from django.contrib.auth.models import User
from django.urls import reverse
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.list_url = '/events/'

    def test_can_list_events(self):
        Event.objects.create(owner=self.user, title='event title')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_event(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post(self.list_url, {'title': 'event title'})
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_event(self):
        response = self.client.post(self.list_url, {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='chris', password='testpassword')
        self.user2 = User.objects.create_user(
            username='kirsty', password='testpass')
        self.event1 = Event.objects.create(
            owner=self.user1, title='a title', description='chris event'
        )
        self.event2 = Event.objects.create(
            owner=self.user2, title='another title', description='kirstys event'
        )
        self.detail_url1 = f'/events/{self.event1.pk}/'
        self.detail_url2 = f'/events/{self.event2.pk}/'

    def test_can_retrieve_event_using_valid_id(self):
        response = self.client.get(self.detail_url1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'a title')

    def test_cannot_retrieve_event_using_invalid_id(self):
        invalid_url = '/events/9999/'
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_event(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(self.detail_url1, {
                                   'title': 'updated title', 'description': 'updated description'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.event1.refresh_from_db()
        self.assertEqual(self.event1.title, 'updated title')

    def test_user_cannot_update_someone_elses_event(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(self.detail_url2, {
                                   'title': 'unauthorized update title', 'description': 'unauthorized update description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.event2.refresh_from_db()
        self.assertNotEqual(self.event2.title, 'unauthorized update title')
