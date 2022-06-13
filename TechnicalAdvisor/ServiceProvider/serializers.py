from rest_framework import serializers
from .models import ServiceProviderProfile, Service 

class ServiceProviderProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceProviderProfile
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
