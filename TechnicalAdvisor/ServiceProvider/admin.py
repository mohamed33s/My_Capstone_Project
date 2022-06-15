import site
from django.contrib import admin
from .models import ServiceProviderProfile ,Service


class ServiceProviderProfileAdmin(admin.ModelAdmin):
    list_display = ('user_model', 'phone', 'user_specialty', 'user_field', 'Service')
    list_filter = ('user_model',)
    search_fields = ('user_model',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_provider', 'service_title', 'service_type', 'service_time')
    list_filter = ('service_title',)
    search_fields = ('service_title',)

admin.site.register(ServiceProviderProfile, ServiceProviderProfileAdmin)
admin.site.register(Service,ServicesAdmin)

