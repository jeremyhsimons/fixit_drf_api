from django.test import TestCase
from django.contrib.auth.models import User
from .models import Star
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class StarListTest(APITestCase):
    """
    A test module for the StarList View
    """
    def setUp(self):
        """
        Create user, profile, and star for test db
        """
        test1 = User.objects.create_user(username='test', password="test123")
        test2 = User.objects.create_user(username='test2', password="test456")
        star1 = Star.objects.create(owner=test1, profile=test2.profile)
        star2 = Star.objects.create(owner=test2, profile=test1.profile)

    def test_get_star_list(self):
        """
        Checks that a user can get a list of stars.
        """
        response = self.client.get('/stars/')
        stars = Star.objects.all()
        self.assertEqual(len(stars), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_star(self):
        """
        Checks that an authorized user can star a profile.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/stars/', {
            'owner': 1,
            'profile': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_duplicate_star(self):
        """
        Checks that users can't star the same profile twice.
        """
        self.client.login(username='test', password="test123")
        response = self.client.post('/stars/', {
            'owner': 1,
            'profile': 2,
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_user_cant_create_star(self):
        """
        Checks that users can't star if they're logged out.
        """
        response = self.client.post('/stars/', {
            'owner': 1,
            'profile': 1,
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StarDetailTest(APITestCase):
    """
    A module of tests for the StarDetail view.
    """
    def setUp(self):
        """
        Create user, profile, and star for test db
        """
        test1 = User.objects.create_user(username='test', password="test123")
        test2 = User.objects.create_user(username='test2', password="test456")
        star1 = Star.objects.create(owner=test1, profile=test2.profile)
        star2 = Star.objects.create(owner=test2, profile=test1.profile)

    def test_can_retrieve_star(self):
        """
        Checks that a user can retrive star
        """
        self.client.login(username='test', password="test123")
        response = self.client.get('/stars/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_star(self):
        """
        Checks that a user can delete a star they own
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/stars/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauth_user_cannot_delete_star(self):
        """
        Checks that stars can't be deleted by unuathorised users.
        """
        response = self.client.delete('/stars/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_delete_others_star(self):
        """
        Checks that a user cannot delete a star they don't own
        """
        self.client.login(username='test', password="test123")
        response = self.client.delete('/stars/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
