from django.urls import path
from . import views

app_name = "client"

urlpatterns = [

    path("clinet-profile/add", views.add_clinet_profile, name="add clinet profile"),
    path("clinet-profile/info", views.list_clinet_profile, name="info clinet profile"),
    path("clinet-profile/update/<clinet_profile_id>", views.update_clinet_profile, name="update clinet profile"),
    path("clinet-profile/delete/<clinet_profile_id>", views.delete_clinet_profile, name="delete clinet profile"),

    path("order/add", views.add_order, name="add order"),
    path("order/all", views.list_order, name="list order"),
    path("order/update/<order_id>", views.update_order, name="update order"),
    path("order/delete/<order_id>", views.delete_order, name="delete order"),

    path("review/add", views.add_review, name="add review"),
    path("review/all", views.list_review, name="list review"),
    path("review/update/<review_id>", views.update_review, name="update review"),
    path("review/delete/<review_id>", views.delete_review, name="delete review"),
]