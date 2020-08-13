from django.urls import path
from region import views

urlpatterns = [
    path("regions/", views.RegionList.as_view()),
    path("regions/<int:id>/", views.RegionRUD.as_view()),
]
