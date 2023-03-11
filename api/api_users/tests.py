from django.test import TestCase,Client
import json
from django.urls import reverse

from wezacare.models import CustomUser

from .serializers import UserSerializer 
from rest_framework.test import APITestCase

#  users test

client = Client()

# get users 
class UsersGetTest(TestCase):
    def setUp(self):
        # create a user object
        self.user =CustomUser.objects.create(
            email="kagwepeter07@gmail.com",
            username="Kagwe",
            phone_number='0707801901',
            first_name='peter',
            last_name='kagwe',
            password='testusermodel')
        # get all users 
    def test_get_list_users(self):
        # Uses the reverse function to get the URL for the endpoint
        response = self.client.get(reverse('register'))
        users = CustomUser.objects.all()
        serializer = UserSerializer(users,many=True)
        # assertions
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,serializer.data)
        self.assertEqual(response.data[0]['email'],
        'kagwepeter07@gmail.com')
        
class UsersGetSingleTest(TestCase):
    
    def setUp(self):
        self.user =CustomUser.objects.create(
            email="kagwepeter07@gmail.com",
            username="Kagwe",
            phone_number='0707801901',
            first_name='peter',
            last_name='kagwe',
            password='testusermodel')
        
        # Sends a GET request to retrieve a user by id
    def test_get_user_by_id(self):

        # Uses the reverse function to get the URL for the endpoint with the user id in the URL path
        response = self.client.get(reverse('user', kwargs={'pk': 1}))
        # Asserts that the response contains the expected username
        self.assertEqual(response.data['username'], 'Kagwe')
    
class UserPostPUTTest(APITestCase):
    def setUp(self):
         self.user_create = CustomUser.objects.create(
            email="juma07@gmail.com",
            username="peter",
            phone_number='0707801906',
            first_name='musa',
            last_name='juma',
            password='testusermodel')
         
         self.user_put = {
            'email':"juma07@gmail.com",
            'username':"musa",
            'phone_number':'0707801906',
            'first_name':'musa',
            'last_name':'juma',
            'password':'testusermodel'
         }
         
         self.user_post = {
            'email':"juma07@gmail.com1",
            'username':"musa1",
            'phone_number':'0707801916',
            'first_name':'musa1',
            'last_name':'juma11',
            'password':'testusermodel'
         }
    # Sends a PUT request to update an existing user
    def test_user_put(self):
        # Uses the reverse function to get the URL for the endpoint with the user id in the URL path
        response = self.client.put(
            reverse('user', kwargs={'pk': self.user_create.id}),
            data=json.dumps(self.user_put),
            content_type='application/json'
        )
        # Asserts that the response contains the expected username
        self.assertEqual(response.data['username'], 'musa')
        
        
    # Sends a POST request to create a new user
    def test_user_post(self):
        # Uses the reverse function to get the URL for the register endpoint
        response = self.client.post(
            reverse('register'),
            data=json.dumps(self.user_post),
            content_type='application/json'
        )
        # Asserts that the response contains the expected username
        self.assertEqual(response.data['username'], 'musa1')
    