from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
# router.register(r'tokens', TokenViewSet,'tokens')

urlpatterns = [
    path('', include(router.urls)),
    # obtain  token 
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    

]