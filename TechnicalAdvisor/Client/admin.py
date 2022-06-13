from ast import Or
from django.contrib import admin
from .models import ClientProfile, Orders , Review

admin.site.register(ClientProfile)
admin.site.register(Orders)
admin.site.register(Review)
