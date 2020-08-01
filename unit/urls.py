from django.urls import path
from unit import views

urlpatterns = [
    path("units/", views.UnitList.as_view()),
    path("units/<int:unitId>/", views.UnitRUD.as_view())
]