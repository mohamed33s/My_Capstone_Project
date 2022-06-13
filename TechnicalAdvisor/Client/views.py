from turtle import title
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import  ClientProfile , Orders , Review
from .serializers import ClientProfileSerializer , OrdrsSerializer , Review, ReviewSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_clinet_profile(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_clinetProfile = ClientProfileSerializer(data=request.data)
    if new_clinetProfile.is_valid():
        new_clinetProfile.save()
        dataResponse = {
            "msg" : "Created Successfully",
            "Your profile:" : new_clinetProfile.data
        }
        return Response(dataResponse)
    else:
        print(new_clinetProfile.errors)
        dataResponse = {"msg" : "couldn't create your profile"}
    return Response( dataResponse, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_clinet_profile(request : Request):

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
def update_clinet_profile(request : Request, clinet_profile_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    profile = ClientProfile.objects.get(id=clinet_profile_id)

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
def delete_clinet_profile(request: Request, clinet_profile_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    profile = ClientProfile.objects.get(id=clinet_profile_id)
    profile.delete()
    return Response({"msg" : "Deleted Successfully"})

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


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_order(request : Request, Order_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    order = Orders.objects.get(id=Order_id)

    uptade_order = OrdrsSerializer(instance=order, data=request.data)
    if uptade_order.is_valid():
        uptade_order.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(uptade_order.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_order(request: Request, order_id):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    order = Orders.objects.get(id=order_id)
    order.delete()
    return Response({"msg" : "Deleted Successfully"})


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


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_review(request : Request, review_is):

    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    review = Review.objects.get(id=review_is)

    uptade_review = ReviewSerializer(instance=review, data=request.data)
    if uptade_review.is_valid():
        uptade_review.save()
        responseData = {
            "msg" : "updated successefully"
        }

        return Response(responseData)
    else:
        print(uptade_review.errors)
        return Response({"msg" : "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_review(request: Request, review_is):
   
    if not request.user.is_authenticated:
        return Response({"msg" : "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    
    review = Review.objects.get(id=review_is)
    review.delete()
    return Response({"msg" : "Deleted Successfully"})




