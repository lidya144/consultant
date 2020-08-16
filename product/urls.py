from django.urls import path
from product import views

urlpatterns = [
    path("regions/", views.ContactinfoList.as_view()),
    path("regions/<int:id>/", views.ContactinfoRUD.as_view()),
]
