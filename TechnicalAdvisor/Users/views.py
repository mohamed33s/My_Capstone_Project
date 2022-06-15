from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from jwt import ExpiredSignatureError
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegisterSerializer

@api_view(['POST'])
def register_user(request : Request):
    '''Through this function, the user is registered by user model in django'''

    user_serializer  = UserRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        return Response({"msg" : "created user successfuly"})
    else:
        print(user_serializer.errors)
        return Response({"msg" : "Couldn't create suer"}, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request : Request):
    '''Through this function, the user is logged in and a token is provided to him'''

    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:

            token = AccessToken.for_user(user)
            responseData = {
                "msg" : "Your token is ready",
                "token" : str(token)
            }
            return Response(responseData)

    return Response({"msg" : "please provide your username & password"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def list_users(request : Request):
    '''Through this function, view all users registered in the system'''
    
    notes = User.objects.all()

    dataResponse = {
        "msg" : "List of All Users",
        "notes" : UserRegisterSerializer(instance=notes, many=True).data
    }

    return Response(dataResponse)
