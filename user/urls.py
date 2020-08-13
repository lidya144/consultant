from django.urls import path
from user import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = "user"

urlpatterns = [
    path("auth/signup/", views.SignupUserView.as_view(), name="signup"),
    path("auth/login/", views.LoginAPIView.as_view(), name="login"),
]
