from django.db import models
from django.contrib.auth.models import User


class ServiceProviderProfile(models.Model):
    User_model = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Birth = models.DateField(blank= False)
    Phone = models.CharField(max_length=12, blank= False)
    User_specialty = models.CharField(max_length=64 , blank= False)
    User_field = models.CharField(max_length=64 , blank= False)
    User_image = models.ImageField(blank= True)
    SERVICE_CHOICES = (
        (1, 'Technical Advice'),
        (2, 'Technical Services'),
        (3, 'Technical Advice and Service'),
    )
    Service =  models.IntegerField (choices=SERVICE_CHOICES, blank= False)

    def __str__(self):
        return self.Phone


class Service(models.Model):
    Service_provider = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    Service_title = models.CharField(max_length=64 , blank= False)
    Service_type = models.CharField(max_length=64 , blank= False)
    Desc= models.TextField(max_length=200)
    Service_time = models.IntegerField(blank= False)
    price = models.DecimalField(max_digits=3, decimal_places=1, blank= False)

    def __str__(self):
        return self.Service_title