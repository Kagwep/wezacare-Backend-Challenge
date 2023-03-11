from django.urls import path
from .views import AnswerList, AnswerDetail

urlpatterns = [
    #users - post and get all
    path('questions/<int:questionId>/answers', AnswerList.as_view(),name='answers'),
    #users get by id , update delete
    path('questions/<int:questionId>/answers/<int:answerId>', AnswerDetail.as_view(),name='answer'),
]