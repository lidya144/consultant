from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="E-Learning documentation")


urlpatterns = [
    path("docs/", schema_view),
    path("admin/", admin.site.urls),
    path("api/v1/", include("grade.urls")),
    path("api/v1/", include("subject.urls")),
    path("api/v1/", include("unit.urls")),
    path("api/v1/", include("category.urls")),
    path("api/v1/", include("language.urls")),
    path("api/v1/", include("user.urls")),
    path("api/v1/", include("transaction.urls")),
    path("api/v1/exams/", include("exam.urls")),
    path("api/v1/quizes/", include("quize.urls")),
]
