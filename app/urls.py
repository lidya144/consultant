from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("grade.urls")),
    path("", include("subject.urls")),
    path("", include("unit.urls")),
    path("", include("category.urls")),
    path("", include("language.urls")),
    path("", include("user.urls")),
    path("", include("transaction.urls")),
    path("exams/", include("exam.urls")),
    path("quizes/", include("quize.urls")),
]
