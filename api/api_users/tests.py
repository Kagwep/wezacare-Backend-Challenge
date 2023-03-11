from django.test import TestCase,Client
import json
from django.urls import reverse

from wezacare.models import CustomUser

from .serializers import UserSerializer 
from rest_framework.test import APITestCase



client = Client()


class UsersGetTest(TestCase):
    def setUp(self):
        self.user =CustomUser.objects.create(
            email="kagwepeter07@gmail.com",
            username="Kagwe",
            phone_number='0707801901',
            first_name='peter',
            last_name='kagwe',
            password='testusermodel')
        
    def test_get_list_users(self):
        response = self.client.get(reverse('register'))
        users = CustomUser.objects.all()
        serializer = UserSerializer(users,many=True)
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

    
    def test_get_user_by_id(self):
        response = self.client.get(reverse('user',kwargs={'pk':1}))
        self.assertEqual(response.data['username'],'Kagwe')
    
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
         
    def test_user_put(self):
        response = self.client.put(
            reverse('user',kwargs={'pk':self.user_create.id}),
            data=json.dumps(self.user_put),
            content_type='application/json'
            
        )
        self.assertEqual(response.data['username'],'musa')
        
    def test_user_post(self):
        response = self.client.post(
            reverse('register'),
            data=json.dumps(self.user_post),
            content_type='application/json'
            
        )
        self.assertEqual(response.data['username'],'musa1')
    