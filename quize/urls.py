from django.urls import include, path
from quize import views


urlpatterns = [
    # path of the choice question of an exam of quizes
    path("choices/", views.ChoiceQuestionList.as_view()),
    path("choices/<int:questionId>/", views.ChoiceQuestionRUD.as_view()),
    # path of the blankspace question of an exam of quizes
    path("blank-spaces/", views.BlankQuestionList.as_view()),
    path("blank-spaces/<int:questionId>/", views.BlankQuestionRUD.as_view()),
    # path of the description question of an exam of quizes
    path("describes/", views.DescribeQuestionList.as_view()),
    path("describes/<int:questionId>/", views.DescribeQuestionRUD.as_view()),
]
