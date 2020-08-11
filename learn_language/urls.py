from django.urls import include, path
from learn_language import views


urlpatterns = [
    path("learn-languanges/", views.LearnLanguageList.as_view()),
    path("learn-languanges/<int:id>/", views.LearnLanguageRUD.as_view()),
    path("l-choices/", views.L_ChoiceQuestionList.as_view()),
    path("l-choices/<int:id>/", views.L_ChoiceQuestionRUD.as_view()),
    path("l-options/", views.L_OptionsList.as_view()),
    path("l-options/<int:id>/", views.L_OptionsRUD.as_view()),
    path("l-options/", views.L_UnitList.as_view()),
    path("l-options/<int:id>/", views.L_UnitRUD.as_view()),
]
