from django.db import models
from django.contrib.auth.models import User
from ServiceProvider.models import ServiceProviderProfile


class ClientProfile(models.Model):
    User_model = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Birth = models.DateField(blank= False)
    Phone = models.CharField(max_length=12, blank= False)
    User_image = models.ImageField(blank= True)

    def __str__(self):
        return self.Phone



class Orders(models.Model):
    Sender_order = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    Recipient_order = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    Order_title = models.CharField(max_length=64 , blank= False)
    Order_type = models.CharField(max_length=64 , blank= False)
    description= models.TextField(blank= False)
    Date_time = models.DateTimeField(auto_now_add=True)
    Order_status = models.CharField(max_length=64, default= 'Waiting')
    

    def __str__(self):
        return self.Order_title


class Review(models.Model):
    Service_provider = models.ForeignKey(ServiceProviderProfile, on_delete=models.CASCADE)
    Username = models.CharField(max_length=64,  blank= False)
    Comment = models.TextField(max_length=200, blank= False)
    Rating = models.IntegerField(choices=[[1, "Wonderful"], [2, "Good"], [3, "Acceptable"]])
    Review_date = models.DateTimeField(auto_now_add=True)
   
    

    def __str__(self):
        return self.Username