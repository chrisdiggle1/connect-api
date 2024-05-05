from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from interested.models import Interested
from events.models import Event


class InterestedListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.interested_url = '/interested/'

    def test_can_list_interested(self):
        Interested.objects.create(owner=self.user, event=self.event)
        response = self.client.get(self.interested_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_confirm_interested(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post(
            self.interested_url, {'event': self.event.id})
        self.assertEqual(Interested.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_confirm_interested(self):
        response = self.client.post(
            self.interested_url, {'event': self.event.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class InterestedDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.interested = Interested.objects.create(
            owner=self.user, event=self.event)
        self.detail_url = f'/interested/{self.interested.pk}/'

    def test_can_retrieve_interested(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_remove_own_interested(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_remove_other_users_interested(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
