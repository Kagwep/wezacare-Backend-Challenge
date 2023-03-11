# from django.shortcuts import render

# # Create your views here.
# from django.forms.models import model_to_dict
# from django.shortcuts import render
# from wezacare.models import CustomUser
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth import authenticate
# from rest_framework import serializers, viewsets,status
# from rest_framework.views import APIView
# # Create your views here.
# class TokenView(APIView):
#     """
#     API endpoint that allows users to obtain a token.
#     """
#     serializer_class = TokenObtainPairSerializer

#     def post(self, request):
#         print("called")
#         print(request.data)
        
#         serializer = self.serializer_class(data=request.data)
       
        
#         serializer.is_valid(raise_exception=True)
        
        
#         username = request.data.get('username')
        
#         print('here',username)
        
#         user_det1 = CustomUser.objects.get(username = username)
        
#         print(user_det1)
        
#         if username is None:
#             return Response({'error': 'username is required'}, status=400)
#         user = get_object_or_404(CustomUser, username=username)
#         print(user)
#         user_det = CustomUser.objects.get(username = user.username)
#         print(user_det)
#         print(username)
#         user_details = model_to_dict(user_det)
#         token = serializer.get_token(user)
#         return Response({
#             'access': str(token.access_token),
#             'refresh': str(token),
#             'user': user_details,
#         })
        
        