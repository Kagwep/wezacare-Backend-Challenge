from django.test import TestCase
from rest_framework.test import APITestCase
import json
from wezacare.models import CustomUser,Question,Answer
from django.urls import reverse
from rest_framework import status

class AnswerPostTest(APITestCase):
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
            username="pet",
            phone_number='070780190',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
     
        
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        
        
        self.answer = Answer.objects.create(
            user_answer = "There are seven days in a week",
            question = self.question,
            user = self.user
        )
        
        self.login = {
            'username':'peter',
            'password':'testusermodel'
            
        }
        
        self.login_1 = {
            'username':'pet',
            'password':'testusermodel'
        }
        
        self.answer_post = {
            "user_answer":"5",
             "questopn":1,
             "user":2
        }
        
        self.url = reverse('token_obtain_pair')
        
        self.response = self.client.post(self.url,self.login,format='json')
        
        self.response_user= self.client.post(self.url,self.login_1,format='json')

    def test_get_answer_question(self):
        url_1 = reverse('answers',kwargs={'questionId':1})

        response_1 = self.client.get(url_1)
        
        self.assertIn('access',self.response.data)
        self.assertEqual(response_1.data[0]['user_answer'],'There are seven days in a week')
        
    def test_post_answer_question(self):
        url = reverse('answers',kwargs={'questionId':1})
        response = self.client.post(
            url,
            data=json.dumps(self.answer_post),
            content_type="application/json",
            
        )
        
        response_1 = self.client.post(
            url,
            data=json.dumps(self.answer_post),
            content_type="application/json",
            HTTP_AUTHORIZATION = 'Bearer ' + self.response_user.data['access']
            
        )
        
       
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_1.data['user_answer'],'5')
    
   
         
         
class AnswerTestCase(APITestCase):
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
            username="pet",
            phone_number='070780190',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
     
        
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        
        
        self.answer = Answer.objects.create(
            user_answer = "There are seven days in a week",
            question = self.question,
            user = self.user
        )
        
        self.login = {
            'username':'peter',
            'password':'testusermodel'
            
        }
        
        self.login_1 = {
            'username':'pet',
            'password':'testusermodel'
        }
        
        self.update_answer = {
            "user_answer":"5",
             "question":1,
             "user":2
        }
        
  
        
        
        self.url = reverse('token_obtain_pair')
        
        self.response = self.client.post(self.url,self.login,format='json')
        
        self.response_user= self.client.post(self.url,self.login_1,format='json')

        
    def test_get_one_question_test(self):
        url= (
            reverse('answer',kwargs={'questionId':1,'answerId':1})
        ) 
        response = self.client.get(url)
        self.assertEqual(response.data['user_answer'],"There are seven days in a week")
        
    def test_put_answer(self):
        
        url= (
            reverse('answer',kwargs={'questionId':1,'answerId':1})
        )
        
        response = self.client.put(
            url,
            data=json.dumps(self.update_answer),
            content_type='application/json'
            )
 
        response_1 = self.client.put(
            url,
            data=json.dumps(self.update_answer),
            content_type='application/json',
            HTTP_AUTHORIZATION = 'Bearer ' + self.response.data['access']
            
            )
        

        
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_1.data['user_answer'],'5')
        
    def test_delete_answer(self):
        response = self.client.delete(
            reverse('answer',kwargs={'questionId':1,'answerId':1}),
            HTTP_AUTHORIZATION = 'Bearer '+ self.response.data['access']
            
        )
        
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
