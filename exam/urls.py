from django.urls import include, path
from exam import views


urlpatterns = [
    # path of the choice question of an exam of quizes
    path("choices/", views.ChoiceQuestionList.as_view()),
    path("choices/<int:questionId>/", views.ChoiceQuestionRUD.as_view()),
    path("options/", views.OptionList.as_view()),
    path("options/<int:id>/", views.OptionRUD.as_view()),
    path("matching-instructions/", views.MatchingInstructionList.as_view()),
    path("matching-questions/", views.MatchingQuestionList.as_view()),
    path("matching-posible-answers/", views.MatchingPosibleAnswerList.as_view()),
    # path of the blankspace question of an exam of quizes
    path("blank-spaces/", views.BlankQuestionList.as_view()),
    path("blank-spaces/<int:questionId>/", views.BlankQuestionRUD.as_view()),
    # path of the description question of an exam of quizes
    path("describes/", views.DescribeQuestionList.as_view()),
    path("describes/<int:questionId>/", views.DescribeQuestionRUD.as_view()),
]
