from django.test import TestCase
from django.contrib.auth.models import User
from .models import PostUpvote
from posts.models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostUpvoteListTest(APITestCase):
    """
    A module of tests for the post upvote list view.
    """
    def setUp(self):
        """
        Create user, post, upvote for test db.
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
        upvote1 = PostUpvote.objects.create(owner=test1, post=post2)
        upvote2 = PostUpvote.objects.create(owner=test2, post=post1)

    def test_get_upvote_list(self):
        """
        Checks that a user can get a list of post upvotes.
        """
        response = self.client.get('/post-upvotes/')
        upvotes = PostUpvote.objects.all()
        self.assertEqual(len(upvotes), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_upvote(self):
        """
        Checks that an authorized user can upvote a post.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/post-upvotes/', {
            'owner': 1,
            'post': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_duplicate_upvote(self):
        """
        Checks that users can't upvote the same post twice.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/post-upvotes/', {
            'owner': 1,
            'post': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_user_cant_create_upvote(self):
        """
        Checks that users can't upvote if they're logged out.
        """
        response = self.client.post('/post-upvotes/', {
            'owner': 1,
            'post': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
