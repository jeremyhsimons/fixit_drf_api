# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Django
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import CommentUpvote
from comments.models import Comment
from posts.models import Post


class CommentUpvoteListTest(APITestCase):
    """
    A test module for the CommentUpvoteList view.
    """
    def setUp(self):
        """
        Create user, post, comment, upvote for test db.
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
        comment1 = Comment.objects.create(
            author=test1,
            post=post2,
            content="This is test comment 1 on post 2"
        )
        comment2 = Comment.objects.create(
            author=test2,
            post=post1,
            content="This is test comment 2 on post 1"
        )
        upvote1 = CommentUpvote.objects.create(owner=test1, comment=comment2)
        upvote2 = CommentUpvote.objects.create(owner=test2, comment=comment1)

    def test_get_upvote_list(self):
        """
        Checks that a user can get a list of comment upvotes.
        """
        response = self.client.get('/comment-upvotes/')
        upvotes = CommentUpvote.objects.all()
        self.assertEqual(len(upvotes), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_upvote(self):
        """
        Checks that an authorized user can upvote a comment.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/comment-upvotes/', {
            'owner': 1,
            'comment': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_duplicate_upvote(self):
        """
        Checks that users can't upvote the same comment twice.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/comment-upvotes/', {
            'owner': 1,
            'comment': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_user_cant_create_upvote(self):
        """
        Checks that users can't upvote if they're logged out.
        """
        response = self.client.post('/comment-upvotes/', {
            'owner': 1,
            'comment': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpvoteCommentDetailTest(APITestCase):
    """
    A module of tests for upvote comment detail view.
    """
    def setUp(self):
        """
        Create user, post, comment, upvote for test db.
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
        comment1 = Comment.objects.create(
            author=test1,
            post=post2,
            content="This is test comment 1 on post 2"
        )
        comment2 = Comment.objects.create(
            author=test2,
            post=post1,
            content="This is test comment 2 on post 1"
        )
        upvote1 = CommentUpvote.objects.create(owner=test1, comment=comment2)
        upvote2 = CommentUpvote.objects.create(owner=test2, comment=comment1)

    def test_can_retrieve_upvote(self):
        """
        Checks that a user can retrive upvote
        """
        self.client.login(username='test', password="test123")
        response = self.client.get('/comment-upvotes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_upvote(self):
        """
        Checks that a user can delete an upvote they own
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/comment-upvotes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauth_user_cannot_delete_upvote(self):
        """
        Checks that upvotes can't be deleted by unuathorised users.
        """
        response = self.client.delete('/comment-upvotes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_delete_others_upvote(self):
        """
        Checks that a user cannot delete an upvote they don't own
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/comment-upvotes/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
