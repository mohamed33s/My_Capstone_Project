from rest_framework import serializers
from .models import ClientProfile, Orders , Review

class ClientProfileSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data ClientProfile '''

    class Meta:
        model = ClientProfile
        fields = '__all__'

class OrdrsSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data Ordrs '''


    class Meta:
        model = Orders
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data Review '''



    class Meta:
        model = Review
        fields = '__all__'