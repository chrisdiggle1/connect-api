from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from followers.models import Follower


class FollowerListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.follow_url = '/followers/'

    def test_can_list_followers(self):
        Follower.objects.create(owner=self.user, followed=self.other_user)
        response = self.client.get(self.follow_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_follow(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post(
            self.follow_url, {'followed': self.other_user.id})
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_follow(self):
        response = self.client.post(
            self.follow_url, {'followed': self.other_user.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.follower = Follower.objects.create(
            owner=self.user, followed=self.other_user)
        self.detail_url = f'/followers/{self.follower.pk}/'

    def test_can_retrieve_follow(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_own_follow(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_follow(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
