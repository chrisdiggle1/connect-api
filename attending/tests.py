from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from attending.models import Attending
from events.models import Event


class AttendingListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )

    def test_can_list_attending(self):
        Attending.objects.create(owner=self.user, event=self.event)
        response = self.client.get('/attending/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_confirm_attending(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post('/attending/', {'event': self.event.id})
        self.assertEqual(Attending.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_confirm_attending(self):
        response = self.client.post('/attending/', {'event': self.event.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AttendingDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.attending = Attending.objects.create(
            owner=self.user, event=self.event)

    def test_can_retrieve_attending(self):
        response = self.client.get(f'/attending/{self.attending.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_delete_own_attending(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.delete(f'/attending/{self.attending.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_attending(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.delete(f'/attending/{self.attending.pk}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
