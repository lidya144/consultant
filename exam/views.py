from django.shortcuts import render
from rest_framework import generics
from models_app.models import (
    ExamChoiceQuestionModel,
    ExamBlankSpaceQuestionModel,
    ExamDescribeQuestionModel,
    ExamMatchQuestionModel,
)
from .serializers import (
    ChoiceQuestionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
    MatchQuestionSerializers,
)


class ChoiceQuestionList(generics.ListCreateAPIView):
    queryset = ExamChoiceQuestionModel.objects.all()
    serializer_class = ChoiceQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class ChoiceQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamChoiceQuestionModel.objects.all()
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
    queryset = ExamBlankSpaceQuestionModel.objects.all()
    serializer_class = BlankQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class BlankQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamBlankSpaceQuestionModel.objects.all()
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
    queryset = ExamMatchQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class DescribeQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamMatchQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)

