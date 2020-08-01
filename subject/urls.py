from django.urls import path
from subject import views

urlpatterns = [
    path("subjects/", views.SubjectList.as_view()),
    path("subjects/<int:subjectId>/", views.SubjectRUD.as_view()),
]
