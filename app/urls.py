from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="E-Learning documentation")

base_url = "api/v1/"

urlpatterns = [
    path("docs/", schema_view),
    path("admin/", admin.site.urls),
    path(base_url, include("grade.urls")),
    path(base_url, include("subject.urls")),
    path(base_url, include("unit.urls")),
    # path(base_url, include("language.urls")),
    path(base_url, include("user.urls")),
    path(base_url, include("general_knowledy.urls")),
    path(base_url, include("learn_language.urls")),
    path(base_url, include("transaction.urls")),
    path(base_url + "exams/", include("exam.urls")),
    path(base_url + "quizes/", include("quize.urls")),
    path(base_url, include("region.urls")),
    path(base_url, include("device.urls")),
]
