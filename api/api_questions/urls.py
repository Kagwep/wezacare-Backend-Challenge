from django.urls import path
from .views import QuestionList, QuestionDetail


urlpatterns = [
    #users - post and get all
    path('questions', QuestionList.as_view(),name='questions'),
    #users get by id , update delete
    path('questions/<int:pk>/', QuestionDetail.as_view(),name='question'),
]