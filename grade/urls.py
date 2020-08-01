from django.urls import include, path
from grade import views

urlpatterns = [
    path("grades/",views.GradeList.as_view()),
    path("grades/<int:gradeId>/",views.GradeRUD.as_view())
    
]