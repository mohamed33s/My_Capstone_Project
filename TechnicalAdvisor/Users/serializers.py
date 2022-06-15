from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    '''from this class the serializer is executed on the model data User '''


    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password', 'is_staff']
