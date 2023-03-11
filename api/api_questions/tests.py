from rest_framework.test import APITestCase
from wezacare.models import Question,CustomUser
from django.urls import reverse
import json
from rest_framework import status


# question test
class QuestionsTest(APITestCase):
    def setUp(self):
        # create a user
        self.user = CustomUser.objects.create(
            email="juma07@gmail.com",
            username="peter",
            phone_number='0707801906',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
        
     
        # create a question
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        # json object of a new questin
        self.new_question ={
            'user_question':'How many Continents are there',
            'user':self.user.id
        }
        
        # json object with login details
        self.login = {
            'username':'peter',
            'password':'testusermodel'
        }
        

            
        # Sends a GET request to retrieve all questions
    def test_get_all_questions(self):
        # Uses the reverse function to get the URL for the endpoint
        response  = self.client.get(reverse('questions'))
        # Uses the reverse function to get the URL for the endpoint question
        self.assertEqual(response.data[0]['user_question'],"How many days are there in a week.")
        
        # Sends a POST request to add a question while unautheticated
    def test_post_question_unauthenticated(self):
        # Uses the reverse function to get the URL for the endpoint
        response = self.client.post(
            reverse('questions'),
            data=json.dumps(self.new_question),
            content_type='application/json'
        )
         # Asserts that the response contains the expected status code
        self.assertEqual(response.status_code,401)
        
      # Sends a POST request to add a question while autheticated   
    def test_post_question_authenticated(self):
        
        # Uses the reverse function to get the URL for the endpoint to obtain token
        url = reverse('token_obtain_pair')
        response = self.client.post(url, self.login, format='json')
        
        
        # Uses the reverse function to get the URL for the endpoint to post
        response1 = self.client.post(
            reverse('questions'),
            data=json.dumps(self.new_question),
            content_type='application/json',
            HTTP_AUTHORIZATION= 'Bearer ' +response.data['access']
        )
        
          # Assert that the response contains the expected user question
        self.assertEqual(response1.data['user_question'],"How many Continents are there")
# class QuestionTest(APITestCase):

# get a question by id 
class QuestionTest(APITestCase):

    def setUp(self):
        # create a user
        self.user = CustomUser.objects.create(
            email="juma07@gmail.com",
            username="peter",
            phone_number='0707801906',
            first_name='musa',
            last_name='juma',
            password='testusermodel'
        )
        # create another user
        self.user_1 = CustomUser.objects.create(
            email="juma7@gmail.com",
            username="musa",
            phone_number='070780190',
            first_name='mus',
            last_name='jum',
            password='testusermodel'
        )
            #  create a question
        self.question = Question.objects.create(
            user_question = "How many days are there in a week.",
            user= self.user
        )
        
        # json object for log in for user 0
        self.login = {
            'username': 'peter',
            'password': 'testusermodel'
        }
        
        # json object for log in for user 1
        self.login_1 = {
            'username': 'musa',
            'password': 'testusermodel'
        }
        # json object to update question
        self.question_update = {
            "user_question":"How many days are there in a week. updated",
            "user":self.user.id
        }
      
# Send a GET request to retrieve question by id
    def test_question_get(self):
          # Use the reverse function to get the URL for the endpoint with the question id in the URL path
        response = self.client.get(
            reverse('question',kwargs={'pk':1}),
            
            )
        # Assert that the response contains the expected user question
        self.assertEqual(response.data['user_question'],"How many days are there in a week.")
 
 # Send a PUT request to update a question while unautheticated and then autheticated 
    def test_question_put(self):
        # Uses the reverse function to get the URL for the endpoint
        url = reverse('token_obtain_pair')
        response = self.client.post(url, self.login, format='json')
        
        # Uses the reverse function to get the URL for the endpoint with the question id in the URL path
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
        
            
            # assertions
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
        
    
    
        
