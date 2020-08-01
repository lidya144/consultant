from django.urls import include, path
from language import views

urlpatterns = [
    path("languages/",views.LanguageList.as_view()),
    path("languages/<int:languageId>/",views.LanguageRUD.as_view())
    
]