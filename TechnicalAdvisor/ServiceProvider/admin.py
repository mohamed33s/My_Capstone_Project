import site
from django.contrib import admin
from .models import ServiceProviderProfile ,Service

admin.site.register(ServiceProviderProfile)
admin.site.register(Service)


