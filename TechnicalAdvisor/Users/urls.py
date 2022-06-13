from django.urls import path
from . import views
from knox import views as knox_views


app_name = "users"

urlpatterns = [

    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("logout", knox_views.LogoutView.as_view(), name='logout'),
    path("user/all", views.list_users, name="list note"),

]