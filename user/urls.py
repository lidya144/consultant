from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("auth/signup/", views.SignupUserView.as_view(), name="signup"),
    path("auth/login/", views.LoginAPIView.as_view(), name="login"),
]
