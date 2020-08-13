from django.urls import path
from device import views

urlpatterns = [
    path("devices/", views.DeviceList.as_view()),
    path("devices/<int:id>/", views.DeviceRUD.as_view()),
]
