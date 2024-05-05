from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from comments.models import Comment
from events.models import Event


class CommentListViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.comment_url = '/comments/'

    def test_can_list_comments(self):
        Comment.objects.create(
            owner=self.user, event=self.event, content="Nice event")
        response = self.client.get(self.comment_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.post(
            self.comment_url, {'event': self.event.id, 'content': 'Nice event'})
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_comment(self):
        response = self.client.post(
            self.comment_url, {'event': self.event.id, 'content': 'Nice event'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='chris', password='testpassword')
        self.other_user = User.objects.create_user(
            username='kirsty', password='testpass')
        self.event = Event.objects.create(
            owner=self.user, title='Test Event', description='Description'
        )
        self.comment = Comment.objects.create(
            owner=self.user, event=self.event, content="Nice event")
        self.detail_url = f'/comments/{self.comment.pk}/'

    def test_can_retrieve_comment(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_update_own_comment(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.put(
            self.detail_url, {'event': self.event.id, 'content': 'Updated comment'})
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_users_comment(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.put(
            self.detail_url, {'event': self.event.id, 'content': 'Updated comment'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_comment(self):
        self.client.login(username='chris', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_comment(self):
        self.client.login(username='kirsty', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
