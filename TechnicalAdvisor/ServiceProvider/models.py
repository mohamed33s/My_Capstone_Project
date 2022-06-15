from django.db import models
from django.contrib.auth.models import User


class ServiceProviderProfile(models.Model):
    '''
    This model contains service providers information details
    '''
    user_model = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    birth = models.DateField(blank= False)
    phone = models.CharField(max_length=12, blank= False)
    user_specialty = models.CharField(max_length=64 , blank= False)
    user_field = models.CharField(max_length=64 , blank= False)
    user_image = models.URLField(blank= True)
    SERVICE_CHOICES = (
        (1, 'Technical Advice'),
        (2, 'Technical Services'),
        (3, 'Technical Advice and Service'),
    )
    Service =  models.IntegerField (choices=SERVICE_CHOICES, blank= False)

    def __str__(self):
        return self.user_model


class Service(models.Model):
    '''
    This model contains everything related to the details of the service
    '''
    service_provider = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    service_title = models.CharField(max_length=64 , blank= False)
    service_type = models.CharField(max_length=64 , blank= False)
    desc= models.TextField(max_length=200)
    service_time = models.IntegerField(blank= False)
    price = models.DecimalField(max_digits=3, decimal_places=1, blank= False)

    def __str__(self):
        return self.service_title