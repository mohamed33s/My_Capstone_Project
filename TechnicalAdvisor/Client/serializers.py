from rest_framework import serializers
from .models import ClientProfile, Orders , Review

class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = '__all__'

class OrdrsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = '__all__'