#from http import server
#from turtle import title
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  ServiceProviderProfile , Service , User
from .serializers import ServiceProviderProfileSerializer , ServiceSerializer
from Users.serializers import UserRegisterSerializer


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_provider_profile(request : Request):
    '''Through this function the service provider profile is added and linked with the user model and executed authentication on the service provider'''


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
    '''Through this function the service provider profile is displayed after executed authentication on the service provider'''


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
    '''Through this function the service provider profile is updated after executed authentication on the service provider'''


    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = ServiceProviderProfile.objects.get(user_model=provider_profile_id)

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
         
    '''Through this function the service provider profile is deleted after executed authentication on the service provider'''

   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    profile = ServiceProviderProfile.objects.get(user_model=provider_profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(["GET"])
def search_provider(request: Request,field):

    '''With this function the service provider profile is searched by field'''

    provider = ServiceProviderProfile.objects.filter(user_field= field ) 
    if provider.exists():
        data = {
        "msg": "Found it",
        "provider":ServiceProviderProfileSerializer(instance=provider, many=True).data 
           }
        return Response(data)
    else:
        return Response({"msg": "Not found!!"})


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_service(request : Request):
    '''Through this function the service is added after executed authentication on the service provider'''


    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_service = ServiceSerializer(data=request.data)
    if new_service.is_valid():
        new_service.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your profile:" : new_service.data
        }
        return Response(dataResponse)
    else:
        print(new_service.errors)
        dataResponse = {"msg" : "couldn't create service"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def list_service(request : Request):
    '''Through this function the services is displayed after executed authentication on the service provider'''


    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      service = Service.objects.all()

      dataResponse = {
        "Your service" : ServiceSerializer(instance=service, many=True).data
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def delete_service(request: Request, service_id):
    '''Through this function the services is deleted after executed authentication on the service provider'''

   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    service = Service.objects.get(id=service_id)
    service.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(["GET"])
def search_service(request: Request, type):
    '''With this function the service is searched by type'''

    service = Service.objects.filter(service_type= type) 
    if service.exists():
        data = {
        "msg": "Found it",
        "service": ServiceSerializer(instance=service, many=True).data
           }
        return Response(data)
    else:
        return Response({"msg": "Not found service!!"})
