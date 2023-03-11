from django.test import TestCase
from .models import CustomUser,Question,Answer

class UserModelTest(TestCase):
    def test_string_representation(self):
        user = CustomUser(username ="kagwe")
        self.assertEqual(str(user),user.username)
        
    def test_userobject_creation(self):
        user = CustomUser.objects.create(email="kagwepeter07@gmail.com",username="Kagwe",phone_number='0707801901',first_name='peter',last_name='kagwe',password='testusermodel')
    
        new_user_in = CustomUser.objects.get(username=user)
        
        self.assertEqual(new_user_in.first_name,"peter")
        
class QuestionModelTest(TestCase):
    def test_string_representation(self):
        question = Question(user_question ="This is a question test")
        self.assertEqual(str(question),question.user_question)
        
    def test_get_question_details(self):
        user = CustomUser.objects.create(email="kagwepeter007@gmail.com",username="peter",phone_number='0707801908',first_name='peter',last_name='kagwe',password='testusermodel')
    
        new_user_in = CustomUser.objects.get(username=user)
        
        self.assertEqual(new_user_in.first_name,"peter")
        
        question = Question.objects.create(user_question="Question get test",user =new_user_in)
        
        self.assertEqual(question.get_question_details(),"Question: " + "Question get test" +" asked by " + "peter")
        
class AnswerModelTest(TestCase):
    
    def test_string_representation(self):
        answer = Answer(user_answer ="this is the answer test")
        self.assertEqual(str(answer),answer.user_answer)
        
        

