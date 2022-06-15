from rest_framework import serializers
from .models import ServiceProviderProfile, Service 

class ServiceProviderProfileSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data ServiceProviderProfile '''


    class Meta:
        model = ServiceProviderProfile
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data Service '''


    class Meta:
        model = Service
        fields = '__all__'
