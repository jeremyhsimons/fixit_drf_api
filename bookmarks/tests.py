from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bookmark
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class BookmarkListViewTest(APITestCase):
    """
    A test module for the bookmark list/create generic view.
    """

    def setUp(self):
        """
        Creates test users, posts, and bookmarks
        for this test module.
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
        Bookmark1 = Bookmark.objects.create(
            owner=test1,
            post=post2
        )
        Bookmark2 = Bookmark.objects.create(
            owner=test2,
            post=post1
        )

    def test_users_can_get_bookmark_list(self):
        """
        Checks that users can return a list of bookmarks
        """
        response = self.client.get('/bookmarks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_auth_user_can_create_bookmark(self):
        """
        Tests that a logged in user can add a bookmark
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/bookmarks/', {
            'owner': 1,
            'post': 1
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_cannot_bookmark_same_post_twice(self):
        """
        Checks that the user can't duplicate a bookmark.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/bookmarks/', {
            'owner': 1,
            'post': 2
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_user_cannot_add_bookmark(self):
        """
        Checks that a user can't bookmark a post when
        they are not logged in.
        """
        response = self.client.post('/bookmarks/', {
            'owner': 1,
            'post': 1
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class BookmarkDetailTest(APITestCase):
    """
    A test suite for bookmark detail view.
    """
    def setUp(self):
        """
        Creates test users, posts, and bookmarks
        for this test module.
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
        Bookmark1 = Bookmark.objects.create(
            owner=test1,
            post=post2
        )
        Bookmark2 = Bookmark.objects.create(
            owner=test2,
            post=post1
        )

    def test_user_can_retrieve_bookmark(self):
        """
        Tests that a user can retrieve bookmark by ID.
        """
        self.client.login(username='test', password="test123")
        response = self.client.get('/bookmarks/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_remove_bookmark(self):
        """
        Checks that a user can delete their own bookmarks.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/bookmarks/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_bookmark(self):
        """
        Checks that users can't delete another user's bookmark.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/bookmarks/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_user_cannot_delete_bookmark(self):
        """
        Checks that users can't delete bookmarks if they
        are not logged in.
        """
        response = self.client.delete('/bookmarks/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
