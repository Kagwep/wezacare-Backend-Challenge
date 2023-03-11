from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from wezacare.models import Answer,Question,CustomUser
from .serializers import AnswerSerializer
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import UserPermission


#get all users / post new user
class AnswerList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (UserPermission,)
    
 

    def get(self, request,questionId):
        #get all users from model
        if Question.objects.filter(id=questionId).exists():
             answers = Answer.objects.filter(question=questionId)
        else:
            raise ValidationError(f"Question with id {questionId} does not exist.")
        #serialize our user objects
        serializer = AnswerSerializer(answers, many=True)
        #return serialized data
        return Response(serializer.data)

    def post(self, request, questionId):
        user_answer = request.data['user_answer']
        if Question.objects.filter(id=questionId).exists():
            question = Question.objects.get(id=questionId)
        else:
            raise ValidationError("Thsis Question does not exist")
        user = request.user

        # Check if the user has already answered the question
        if Answer.objects.filter(user=user, question=question).exists():
            raise ValidationError("You have already answered this question.")
        
                # Check if the user has already answered the question    

        new_answer = Answer.objects.create(
            user_answer=user_answer,
            question=question,
            user=request.user
        )

        serializer = AnswerSerializer(new_answer,many=False)

        
            
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AnswerDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (UserPermission,)

    # Retrieve, update or delete a user instance

    # #get user
    # def get_object(self, questionId,answerId):
    #     try:
    #         return Answer.objects.get(question=questionId,id=answerId)
    #     except Answer.DoesNotExist:
    #         raise Http404
        
     #get user by id
    def get(self, request, questionId,answerId):
        
        ques = Question.objects.filter(id=questionId).exists()
        ans = Answer.objects.filter(id=answerId).exists()
        
        if ques and ans:
            answer= Answer.objects.get(id=answerId,question=questionId)
            serializer = AnswerSerializer(answer)
            
            return Response(serializer.data)      
        else:
            raise ValidationError(f"Something is wrong.Check question or answer id.")


 
    #update the fields of requested object id
    def put(self, request, questionId,answerId):
        answer = Answer.objects.get(question=questionId,id=answerId)

        # Only update fields that were provided
        if 'user_answer' in request.data:
            answer.user_answer = request.data['user_answer']

        #save the update
        answer.save()

         #serialize the user
        serializer = AnswerSerializer(answer)
         # return the updated data
        return Response(serializer.data)

    #get the user by id
    def delete(self, request, questionId,answerId):
        answer = Answer.objects.get(question=questionId,id=answerId)
        #delete the user
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
