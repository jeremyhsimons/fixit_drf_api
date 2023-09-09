from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class CommentListViewTests(APITestCase):
    """
    A module containing all tests for the comment list view
    """
    def setUp(self):
        """
        Creates test users for this test module.
        """
        test1 = User.objects.create_user(username='test', password="test123")
        test2 = User.objects.create_user(username='test2', password="test456")
        Post.objects.create(
            author=test1,
            content="this is test1's post",
            category="BC"
        )
        Post.objects.create(
            author=test2,
            content="this is test2's post",
            category="BC"
        )

    def test_can_view_comment_list(self):
        """
        Tests that a user can successfully get comments list
        from the api.
        """
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_user_can_create_comment(self):
        """
        Tests that a user can write a comment
        on a post when they are logged in.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/comments/', {
            'author': 1,
            'post': 1,
            'content': "This is a comment"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_non_auth_user_cannot_create_comment(self):
        """
        Tests that a user cannot comment if they are not
        logged in.
        """
        response = self.client.post('/comments/', {
            'author': 1,
            'post': 1,
            'content': "This is a comment"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# class CommentDetailViewTests(APITestCase):
