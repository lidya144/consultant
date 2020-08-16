from django.urls import path
from product import views

urlpatterns = [
    path("contacts/", views.ContactinfoList.as_view()),
    path("contacts/<int:id>/", views.ContactinfoRUD.as_view()),
]
