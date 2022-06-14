from turtle import title
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  ClientProfile , Orders , Review , User
from .serializers import ClientProfileSerializer , OrdrsSerializer , ReviewSerializer
from Users.serializers import UserRegisterSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_client_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_clientProfile = ClientProfileSerializer(data=request.data)
    if new_clientProfile.is_valid():
        new_clientProfile.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your profile:" : new_clientProfile.data
        }
        return Response(dataResponse)
    else:
        print(new_clientProfile.errors)
        dataResponse = {"msg" : "couldn't create your profile"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_client_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      profile = ClientProfile.objects.all() 

      dataResponse = {
        "Your profile" : ClientProfileSerializer(instance=profile, many=True).data 
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_client_profile(request : Request, client_profile_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = ClientProfile.objects.get(User_model=client_profile_id)

    uptade_profile = ClientProfileSerializer(instance=profile, data=request.data)
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
def delete_client_profile(request: Request, client_profile_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    profile = ClientProfile.objects.get(User_model=client_profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})



@api_view(["GET"])
def search_client(request: Request, name):
    client = User.objects.filter(first_name= name)  #ClientProfile.objects.filter(Phone= phone ) #
    if client.exists():
        data = {
        "msg": "Found it",
        "client": UserRegisterSerializer(instance=client, many=True).data #ClientProfileSerializer(instance=client, many=True).data # 
           }
        return Response(data)
    else:
        return Response({"msg": "Not found!!"})

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_order(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_order = OrdrsSerializer(data=request.data)
    if new_order.is_valid():
        new_order.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your order" : new_order.data
        }
        return Response(dataResponse)
    else:
        print(new_order.errors)
        dataResponse = {"msg" : "couldn't create a Order"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_order(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      order = Orders.objects.all()

      dataResponse = {
        "msg" : "List of All Orders",
        "Your orders" : OrdrsSerializer(instance=order, many=True).data
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_order(request: Request, order_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    order = Orders.objects.get(id=order_id)
    order.delete()
    return Response({"msg" : "Deleted Successfully"})


@api_view(["GET"])
def search_orders(request: Request, title):
    order = Orders.objects.filter(Order_title= title) 
    if order.exists():
        data = {
        "msg": "Found it",
        "order": OrdrsSerializer(instance=order, many=True).data
           }
        return Response(data)
    else:
        return Response({"msg": "Not found order!!"})


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_review(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_review = ReviewSerializer(data=request.data)
    if new_review.is_valid():
        new_review.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your review" : new_review.data
        }
        return Response(dataResponse)
    else:
        print(new_review.errors)
        dataResponse = {"msg" : "couldn't create a Order"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_review(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    else:
      review = Review.objects.all()

      dataResponse = {
        "msg" : "List of All Reviws",
        "Reviews" : ReviewSerializer(instance=review, many=True).data
        }
    return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_review(request: Request, review_is):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    review = Review.objects.get(id=review_is)
    review.delete()
    return Response({"msg" : "Deleted Successfully"})




