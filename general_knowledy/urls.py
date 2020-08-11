from django.urls import include, path
from general_knowledy import views


urlpatterns = [
    path("general-knowledy/", views.GeneralKnowledgyList.as_view()),
    path("general-knowledy/<int:id>/", views.GeneralKnowledgyRUD.as_view()),
    path("g-choice/", views.G_ChoiceQuestionList.as_view()),
    path("g-choice/<int:id>/", views.G_ChoiceQuestionRUD.as_view()),
    path("g-options/", views.G_OptionsList.as_view()),
    path("g-options/<int:id>/", views.G_OptionsRUD.as_view()),
    path("g-options/", views.G_UnitList.as_view()),
    path("g-options/<int:id>/", views.G_UnitRUD.as_view()),
]
