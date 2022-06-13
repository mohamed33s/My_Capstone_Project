from turtle import title
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  ServiceProviderProfile , Service 
from .serializers import ServiceProviderProfileSerializer , ServiceSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_provider_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_providerProfile = ServiceProviderProfileSerializer(data=request.data)
    if new_providerProfile.is_valid():
        new_providerProfile.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your profile:" : new_providerProfile.data
        }
        return Response(dataResponse)
    else:
        print(new_providerProfile.errors)
        dataResponse = {"msg" : "couldn't create your profile"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def info_provider_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      profile = ServiceProviderProfile.objects.all()

      dataResponse = {
        "Your profile" : ServiceProviderProfileSerializer(instance=profile, many=True).data
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_provider_profile(request : Request, provider_profile_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = ServiceProviderProfile.objects.get(id=provider_profile_id)

    uptade_profile = ServiceProviderProfileSerializer(instance=profile, data=request.data)
    if uptade_profile.is_valid():
        uptade_profile.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(uptade_profile.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_provider_profile(request: Request, provider_profile_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    profile = ServiceProviderProfile.objects.get(id=provider_profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_servece(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_servece = ServiceSerializer(data=request.data)
    if new_servece.is_valid():
        new_servece.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your profile:" : new_servece.data
        }
        return Response(dataResponse)
    else:
        print(new_servece.errors)
        dataResponse = {"msg" : "couldn't create servece"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def list_servece(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      servece = Service.objects.all()

      dataResponse = {
        "Your servece" : ServiceSerializer(instance=servece, many=True).data
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def update_servece(request : Request, servece_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    servece = Service.objects.get(id=servece_id)

    uptade_servece = ServiceSerializer(instance=servece, data=request.data)
    if uptade_servece.is_valid():
        uptade_servece.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(uptade_servece.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def delete_servece(request: Request, servece_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    servece = Service.objects.get(id=servece_id)
    servece.delete()
    return Response({"msg" : "Deleted Successfully"})
