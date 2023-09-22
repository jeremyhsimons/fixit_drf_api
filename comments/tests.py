# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import Comment
from posts.models import Post


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


class CommentDetailViewTests(APITestCase):
    """
    A suite of tests for the comment detail view.
    """
    def setUp(self):
        """
        Creates test users for this test module.
        """
        test1 = User.objects.create_user(username='test', password="test123")
        test2 = User.objects.create_user(username='test2', password="test456")
        post1 = Post.objects.create(
            author=test1,
            content="this is test1's post",
            category="BC"
        )
        post2 = Post.objects.create(
            author=test2,
            content="this is test2's post",
            category="BC"
        )
        Comment.objects.create(
            author=test1,
            post=post2,
            content="This is test comment 1 on post 2"
        )
        Comment.objects.create(
            author=test2,
            post=post1,
            content="This is test comment 2 on post 1"
        )

    def test_user_can_retrieve_comment_by_id(self):
        """
        Tests a user can get a single comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.get('/comments/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_edit_comment(self):
        """
        Tests a user can edit their own comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.put('/comments/1', {
            'author': 1,
            'content': "UPDATED COMMENT"
        })
        comment = Comment.objects.filter(pk=1)[0]
        self.assertEqual(comment.content, "UPDATED COMMENT")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_edit_other_users_comment(self):
        """
        Tests that a user can't edit someone elses comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.put('/comments/2', {
            'author': 2,
            'content': "UPDATED COMMENT"
        })
        comment = Comment.objects.filter(pk=2)[0]
        self.assertNotEqual(comment.content, "UPDATED COMMENT")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_comment(self):
        """
        Tests that a user can delete their own comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/comments/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_others_comment(self):
        """
        Tests that a user can't delete
        someone elses' comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/comments/2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_user_cannot_edit_comment(self):
        """
        Tests that an unauthorised user cannot tamper
        with users comments.
        """
        response = self.client.put('/comments/2', {
            'author': 2,
            'content': "UPDATED COMMENT"
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_user_cannot_delete_comment(self):
        """
        Tests that an unauthorised user can't delete
        someone's comment.
        """
        response = self.client.delete('/comments/2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
