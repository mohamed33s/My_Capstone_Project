from django.urls import path
from . import views

app_name = "service_provider"

urlpatterns = [

# all this paths personal of service provider profile
    path("provider-profile/add", views.add_provider_profile, name="add provider profile"),
    path("provider-profile/info", views.info_provider_profile, name="info provider profile"),
    path("provider-profile/update/<provider_profile_id>", views.update_provider_profile, name="update provider profile"),
    path("provider-profile/delete/<provider_profile_id>", views.delete_provider_profile, name="delete provider profile"),
    path("provider-search/<field>", views.search_provider, name = "search provider"),

# all this paths personal of service
    path("service/add", views.add_service, name="Add service"),
    path("service/all", views.list_service, name="list service"),
    path("service/delete/<service_id>", views.delete_service, name="delete service"),
    path("service-search/<field>", views.search_service, name = "search service"),
]