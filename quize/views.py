from django.shortcuts import render
from rest_framework import generics
from models_app.models import (
    QuizeChoiceQuestionModel,
    QuizeBlankSpaceQuestionModel,
    QuizeDescribeQuestionModel,
    QuizeMatchingInstructionModel,
    QuizeMatchingQuestionModel,
    QuizeMatchingPosibleAnswersModels,
)
from .serializers import (
    ChoiceQuestionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
    MatchingInstructionSerializers,
    MatchingQuestionSerializers,
    MatchingPosibleAnswersSerializers,
)


class ChoiceQuestionList(generics.ListCreateAPIView):
    queryset = QuizeChoiceQuestionModel.objects.all()
    serializer_class = ChoiceQuestionSerializers
    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class ChoiceQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizeChoiceQuestionModel.objects.all()
    serializer_class = ChoiceQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)


class MatchingInstructionList(generics.ListCreateAPIView):
    queryset = QuizeMatchingInstructionModel.objects.all()
    serializer_class = MatchingInstructionSerializers


class MatchingQuestionList(generics.ListCreateAPIView):
    queryset = QuizeMatchingQuestionModel.objects.all()
    serializer_class = MatchingQuestionSerializers


class MatchingPosibleAnswerList(generics.ListCreateAPIView):
    queryset = QuizeMatchingPosibleAnswersModels.objects.all()
    serializer_class = MatchingPosibleAnswersSerializers


class ChoiceQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizeChoiceQuestionModel.objects.all()
    serializer_class = ChoiceQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)


"""This the fill the blank question exams of quizes"""


class BlankQuestionList(generics.ListCreateAPIView):
    queryset = QuizeBlankSpaceQuestionModel.objects.all()
    serializer_class = BlankQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class BlankQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizeBlankSpaceQuestionModel.objects.all()
    serializer_class = BlankQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)


"""This is Description portion of the exams or quizes"""


class DescribeQuestionList(generics.ListCreateAPIView):
    queryset = QuizeDescribeQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class DescribeQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizeDescribeQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)

