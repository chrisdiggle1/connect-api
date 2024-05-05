from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from events.models import Event
from followers.models import Follower


class ProfileListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        Event.objects.create(
            owner=self.user, title='Test Event', description='Description')
        self.profile_url = '/profiles/'

    def test_can_list_profiles(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profiles_include_events_count(self):
        response = self.client.get(self.profile_url)
        chris_profile = next(p for p in response.data if p['owner'] == 'chris')
        self.assertEqual(chris_profile['events_count'], 1)

    def test_profiles_include_followers_count(self):
        Follower.objects.create(owner=self.other_user, followed=self.user)
        response = self.client.get(self.profile_url)
        chris_profile = next(p for p in response.data if p['owner'] == 'chris')
        self.assertEqual(chris_profile['followers_count'], 1)

    def test_profiles_include_following_count(self):
        Follower.objects.create(owner=self.user, followed=self.other_user)
        response = self.client.get(self.profile_url)
        chris_profile = next(p for p in response.data if p['owner'] == 'chris')
        self.assertEqual(chris_profile['following_count'], 1)


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.profile = self.user.profile
        self.other_profile = self.other_user.profile
        self.detail_url = f'/profiles/{self.profile.pk}/'
        self.other_detail_url = f'/profiles/{self.other_profile.pk}/'

    def test_can_retrieve_profile(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_own_profile(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(self.detail_url, {'name': 'Updated Name'})
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.name, 'Updated Name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_users_profile(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(self.other_detail_url, {
                                   'name': 'Updated Name'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
