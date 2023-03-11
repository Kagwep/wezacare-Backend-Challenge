
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.api_users.urls')),
    path('api/',include('api.api_questions.urls')),
    path('api/',include('api.api_answers.urls')),
    path('api/',include('api.api_tokens.urls'))
]
