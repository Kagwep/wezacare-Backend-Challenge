from django.urls import path
from .views import QuestionList, QuestionDetail


urlpatterns = [
    #questions - post and get all
    path('questions', QuestionList.as_view(),name='questions'),
    #questions get by id , update delete
    path('questions/<int:pk>/', QuestionDetail.as_view(),name='question'),
]