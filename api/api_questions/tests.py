from rest_framework.test import APITestCase
from wezacare.models import Question,CustomUser
from django.urls import reverse
import json
from rest_framework import status



class QuestionsTest(APITestCase):
    def setUp(self):
        
        self.user = CustomUser.objects.create(
            email="juma07@gmail.com",
            username="peter",
            phone_number='0707801906',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
        
     
        
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        
        self.new_question ={
            'user_question':'How many Continents are there',
            'user':self.user.id
        }
        
        self.login = {
            'username':'peter',
            'password':'testusermodel'
        }
        

            
        
    def test_get_all_questions(self):
        response  = self.client.get(reverse('questions'))
        self.assertEqual(response.data[0]['user_question'],"How many days are there in a week.")
        
    def test_post_question_unauthenticated(self):
        response = self.client.post(
            reverse('questions'),
            data=json.dumps(self.new_question),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code,401)
         
    def test_post_question_authenticated(self):
        
        url = reverse('token_obtain_pair')
        
        response = self.client.post(url, self.login, format='json')
        
        
        
        response1 = self.client.post(
            reverse('questions'),
            data=json.dumps(self.new_question),
            content_type='application/json',
            HTTP_AUTHORIZATION= 'Bearer ' +response.data['access']
        )
        
        
        self.assertEqual(response1.data['user_question'],"How many Continents are there")
# class QuestionTest(APITestCase):
    
class QuestionTest(APITestCase):

    def setUp(self):
        
        self.user = CustomUser.objects.create(
            email="juma07@gmail.com",
            username="peter",
            phone_number='0707801906',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
        self.user_1 = CustomUser.objects.create(
            email="juma7@gmail.com",
            username="musa",
            phone_number='070780190',
            first_name='mus',
            last_name='jum',
            password='testusermodel'
        )
                
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        
        self.login = {
            'username': 'peter',
            'password': 'testusermodel'
        }
        
        self.login_1 = {
            'username': 'musa',
            'password': 'testusermodel'
        }
        
        self.question_update = {
            "user_question":"How many days are there in a week. updated",
            "user":self.user.id
        }
      

    def test_question_get(self):
        
        response = self.client.get(
            reverse('question',kwargs={'pk':1}),
            
            )
        self.assertEqual(response.data['user_question'],"How many days are there in a week.")
        
    def test_question_put(self):
        url = reverse('token_obtain_pair')
        
        response = self.client.post(url, self.login, format='json')
        
        response_1 = self.client.put(
            reverse('question',kwargs={'pk':1}),
            data=json.dumps(self.question_update),
            content_type='application/json',
            HTTP_AUTHORIZATION= 'Bearer ' +response.data['access']
            
        )
        
        response_not_owner = self.client.post(url, self.login_1, format='json')
        
        response_2 = self.client.put(
            reverse('question',kwargs={'pk':1}),
            data=json.dumps(self.question_update),
            content_type='application/json',
            HTTP_AUTHORIZATION= 'Bearer ' +response_not_owner.data['access']
        )
        
        print(response_1.data)
        print(response_2.data)
   
        self.assertIn('access',response.data)
        self.assertEqual(response_1.data['user_question'],"How many days are there in a week. updated")
        self.assertEqual(response_2.data['message'],'You are not the author of the question')
        
    def test_question_delete(self):
        url = reverse('token_obtain_pair')
        
        response = self.client.post(url, self.login, format='json')
        # response_not_owner = self.client.post(url, self.login_1, format='json')
        
        
        response_1 = self.client.delete(
            reverse('question',kwargs={'pk':1}),
            HTTP_AUTHORIZATION = 'Bearer ' +response.data['access']
        )
        
        # response_2 = self.client.delete(
        #     reverse('question',kwargs={'pk':1}),
        #     HTTP_AUTHORIZATION = 'Bearer ' +response_not_owner.data['access']
        # )
        
        self.assertEqual(response_1.status_code,status.HTTP_204_NO_CONTENT)
        # self.assertEqual(response_2.status,status.HTTP_204_NO_CONTENT)
        
    
    
        
