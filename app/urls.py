from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="E-Learning documentation")

base_url = ""

urlpatterns = [
    path("docs/", schema_view),
    path(base_url, admin.site.urls),
    path(base_url, include("grade.urls")),
    path(base_url, include("subject.urls")),
    path(base_url, include("unit.urls")),
    path(base_url, include("category.urls")),
    path(base_url, include("language.urls")),
    path(base_url, include("user.urls")),
    path(base_url, include("transaction.urls")),
    path(base_url + "exams/", include("exam.urls")),
    path(base_url + "quizes/", include("quize.urls")),
]
