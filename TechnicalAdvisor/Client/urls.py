from django.urls import path
from . import views

app_name = "client"

urlpatterns = [

    path("client-profile/add", views.add_client_profile, name="add client profile"),
    path("client-profile/info", views.list_client_profile, name="info client profile"),
    path("client-profile/update/<client_profile_id>", views.update_client_profile, name="update client profile"),
    path("client-profile/delete/<client_profile_id>", views.delete_client_profile, name="delete client profile"),
    path("client-search/<name>", views.search_client, name = "search client"),
    #path("client-search/<phone>", views.search_client, name = "search client"),

    path("order/add", views.add_order, name="add order"),
    path("order/all", views.list_order, name="list order"),
    path("order/delete/<order_id>", views.delete_order, name="delete order"),
    path("order-search/<title>", views.search_orders, name = "search order"),

    path("review/add", views.add_review, name="add review"),
    path("review/all", views.list_review, name="list review"),
    path("review/delete/<review_id>", views.delete_review, name="delete review"),
]