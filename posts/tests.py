from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Creates test users for this test module.
        """
        User.objects.create_user(username='test', password="test123")
        User.objects.create_user(username='test2', password="test456")

    def test_list_posts(self):
        """
        Tests that a user can successfully retrieve
        a list of posts.
        """
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthenticated_cannot_create_post(self):
        """
        Tests that users cannot post if they are not logged in.
        """
        response = self.client.post(
            '/posts/', {
                'content': 'this is a test post',
                'category': 'BC'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_create_post(self):
        """
        Tests that an authenticated user can
        create a post.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post(
            '/posts/', {
                'content': 'this is a test post',
                'category': 'BC',
                'author': 1
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        post = Post.objects.filter(pk=1)
        self.assertEqual(post[0].content, 'this is a test post')


class PostDetailViewTests(APITestCase):
    """
    A test module for the PostDetail view.
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

    def test_can_retrieve_post_by_id(self):
        """
        Tests that a user can fetch a specific post. 
        """
        self.client.login(username='test', password="test123")
        response = self.client.get("/posts/2/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_edit_own_post(self):
        """
        Tests that an authenticated user can
        edit a post that belongs to them
        """
        self.client.login(username='test', password="test123")
        response = self.client.put(
            '/posts/1/', {
                'content': 'this is an updated test post',
                'category': 'EC',
                'author': 1
            }
        )
        post = Post.objects.filter(pk=1)
        self.assertEqual(post[0].content, 'this is an updated test post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_edit_other_users_post(self):
        """
        Tests that a user can't update a post
        that doesn't belong to them.
        """
        self.client.login(username='test', password="test123")
        response = self.client.put(
            '/posts/2/', {
                'content': 'this is an altered test post',
                'category': 'EC',
                'author': 2
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_post(self):
        """
        Checks that an authorised user can delete their own posts.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete("/posts/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_other_users_posts(self):
        """
        Checks that users cannot delete other users' posts.
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete("/posts/2/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_cannot_delete_post(self):
        """
        Checks that unauthenticated users cannot delete posts.
        """
        response = self.client.delete("/posts/2/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_cannot_delete_post(self):
        """
        Checks that unauthenticated users cannot delete posts.
        """
        response = self.client.put(
            '/posts/2/', {
                'content': 'this is an altered test post',
                'category': 'EC',
                'author': 2
            }
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
