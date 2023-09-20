from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """
    A suite of tests for the profile list view.
    """
    def setUp(self):
        """
        Creates test users for test module
        """
        User.objects.create_user(username='test', password="test123")
        User.objects.create_user(username='test2', password="test456")

    def test_can_list_profiles(self):
        """
        Test that the user can retrieve profile list
        """
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailTests(APITestCase):
    """
    A module for profile detail view tests
    """
    def setUp(self):
        """
        Creates test users for test module
        """
        User.objects.create_user(username='test', password="test123")
        User.objects.create_user(username='test2', password="test456")

    def test_can_retrieve_profile(self):
        """
        Checks that a user can get a single profile.
        """
        self.client.login(username='test', password="test123")
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_edit_own_profile(self):
        """
        Test user can update their own profile.
        Status field is required.
        """
        self.client.login(username='test', password="test123")
        response = self.client.put(
            '/profiles/1/', {'bio': 'This is a new bio', "status": "NA"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_edit_other_profile(self):
        """
        Test that the user cannot update
        another user's profile.
        """
        self.client.login(username='test', password="test123")
        response = self.client.put(
            '/profiles/2/', {'name': 'This is a new bio'}
        )
        profile = Profile.objects.filter(pk=2).first()
        self.assertEqual(profile.bio, '')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_user_cannot_edit_profile(self):
        """
        Checks that a user can't edit a profile if they're
        not logged in.
        """
        response = self.client.put(
            '/profiles/2/', {'name': 'This is a new bio'}
        )
        profile = Profile.objects.filter(pk=2).first()
        self.assertEqual(profile.bio, '')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
