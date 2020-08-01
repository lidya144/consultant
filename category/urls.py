from django.urls import include, path
from category import views
urlpatterns = [
    path("categories/",views.CategoryList.as_view()),
    path("categories/<int:categoryId>/",views.CategoryRUD.as_view())
    
]
