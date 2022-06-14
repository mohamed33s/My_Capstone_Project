from django.urls import path
from . import views

app_name = "service_provider"

urlpatterns = [

    path("provider-profile/add", views.add_provider_profile, name="add provider profile"),
    path("provider-profile/info", views.info_provider_profile, name="info provider profile"),
    path("provider-profile/update/<provider_profile_id>", views.update_provider_profile, name="update provider profile"),
    path("provider-profile/delete/<provider_profile_id>", views.delete_provider_profile, name="delete provider profile"),
    #path("provider-search/<name>", views.search_provider, name = "search provider"),
    path("provider-search/<field>", views.search_provider, name = "search provider"),

    path("servece/add", views.add_servece, name="Add servece"),
    path("servece/all", views.list_servece, name="list servece"),
    path("servece/delete/<servece_id>", views.delete_servece, name="delete servece"),
    path("servece-search/<field>", views.search_servece, name = "search servece"),
]