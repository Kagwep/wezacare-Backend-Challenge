from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from wezacare.models import Question
from .serializers import QuestionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission

#get all question / post new question
class QuestionList(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = (UserPermission,)
    

    def get(self, request):
        #get all questions from model
        questions = Question.objects.all()
        #serialize our question objects
        serializer = QuestionSerializer(questions, many=True)
        #return serialized data
        return Response(serializer.data)

    def post(self, request):
        #use our serializer class to serialize data from request
        user_question = request.data['user_question']
        
        # add question
        new_question = Question.objects.create(
            user_question=user_question,
            user=request.user
        )

        serializer = QuestionSerializer(new_question,many=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class QuestionDetail(APIView):

    # Retrieve, update or delete a question instance
    authentication_classes = [JWTAuthentication]
    permission_classes = (UserPermission,)

    #get question
    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise Http404
        
     #get question by id
    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

 
    #update the fields of requested object id
    def put(self, request, pk):
        question = Question.objects.get(id=pk)
        
        if request.user != question.user:
            error_message = {
                'message':'You are not the author of the question' 
            }
            return Response(error_message,status=status.HTTP_400_BAD_REQUEST)

        # Only update fields that were provided
        if 'user_question' in request.data:
            question.user_question = request.data['user_question']

        #save the update
        question.save()
        
        # print(question)

         #serialize the question
        serializer = QuestionSerializer(question)
         # return the updated data
        return Response(serializer.data)

    #get the question by id
    def delete(self, request, pk):
        question = Question.objects.get(id=pk)
        #delete the question
        
        if request.user != question.user:
            error_message = {
                'message':'unauthorised!!'
                }
            return Response(error_message,status=status.HTTP_400_BAD_REQUEST)
        
        question.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
