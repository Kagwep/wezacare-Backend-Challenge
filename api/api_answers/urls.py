from django.urls import path
from .views import AnswerList, AnswerDetail

urlpatterns = [
    #answers - post and get by question id
    path('questions/<int:questionId>/answers', AnswerList.as_view(),name='answers'),
    #answers get by id , update delete
    path('questions/<int:questionId>/answers/<int:answerId>', AnswerDetail.as_view(),name='answer'),
]