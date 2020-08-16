from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views

schema_view = get_swagger_view(title="E-Learning documentation")

base_url = "api/v1/"

urlpatterns = [
    path("docs/", schema_view),
    path("admin/", admin.site.urls),
    path(base_url, include("product.urls")),
    path(base_url, include("user.urls")),
    path(
        "reset_password/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
