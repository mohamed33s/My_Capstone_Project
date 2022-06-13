from django.urls import path
from . import views

app_name = "service_provider"

urlpatterns = [

    path("provider-profile/add", views.add_provider_profile, name="add provider profile"),
    path("provider-profile/info", views.info_provider_profile, name="info provider profile"),
    path("provider-profile/update/<provider_profile_id>", views.update_provider_profile, name="update provider profile"),
    path("provider-profile/delete/<provider_profile_id>", views.delete_provider_profile, name="delete provider profile"),

    path("servece/add", views.add_servece, name="Add servece"),
    path("servece/all", views.list_servece, name="list servece"),
    path("servece/update/<servece_id>", views.update_servece, name="update servece"),
    path("servece/delete/<servece_id>", views.delete_servece, name="delete servece"),
]