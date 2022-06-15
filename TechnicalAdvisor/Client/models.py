from django.db import models
from django.contrib.auth.models import User
from ServiceProvider.models import ServiceProviderProfile


class ClientProfile(models.Model):
    '''
    This model contains client information details
    '''
    user_model = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    birth = models.DateField(blank= False)
    phone = models.CharField(max_length=12, blank= False)
    user_image = models.URLField(blank= True)


    def __str__(self):
        return self.user_model


class Orders(models.Model):
    '''
    This model contains everything related to the details of the order
    '''
    sender_order = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    recipient_order = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    order_title = models.CharField(max_length=64 , blank= False)
    order_type = models.CharField(max_length=64 , blank= False)
    description= models.TextField(blank= False)
    date_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=64, default= 'Waiting')
    

    def __str__(self):
        return self.order_title


class Review(models.Model):
    '''This model is for the comments and ratings attached to the service provider'''
    service_provider = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    username = models.CharField(max_length=64,  blank= False)
    comment = models.TextField(max_length=200, blank= False)
    rating = models.IntegerField(choices=[[1, "Wonderful"], [2, "Good"], [3, "Acceptable"]])
    review_date = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return self.username