from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from reviews.models import Review
from events.models import Event


class ReviewListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword'
        )
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.review_url = '/reviews/'

    def test_can_list_reviews(self):
        Review.objects.create(
            owner=self.user, event=self.event, review="Great event!"
        )
        response = self.client.get(self.review_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_review(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post(
            self.review_url, {'event': self.event.id, 'review': 'Great event!'}
        )
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_review(self):
        response = self.client.post(
            self.review_url, {'event': self.event.id, 'review': 'Great event!'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ReviewDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword'
        )
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass'
        )
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.review = Review.objects.create(
            owner=self.user, event=self.event, review="Great event!"
        )
        self.detail_url = f'/reviews/{self.review.pk}/'

    def test_can_retrieve_review(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_own_review(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(
            self.detail_url, {
                'event': self.event.id,
                'review': 'Updated review'
            }
        )
        self.review.refresh_from_db()
        self.assertEqual(self.review.review, 'Updated review')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_users_review(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.put(
            self.detail_url, {
                'event': self.event.id,
                'review': 'Updated review'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_review(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_review(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
