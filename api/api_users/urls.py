from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    #users - post and get all
    path('auth/register', UserList.as_view(),name='register'),
    #users get by id , update delete
    path('users/<int:pk>/', UserDetail.as_view(),name='user'),
]
