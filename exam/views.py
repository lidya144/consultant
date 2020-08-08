from django.shortcuts import render
from rest_framework import generics
from models_app.models import (
    ExamChoiceQuestionModel,
    ExamBlankSpaceQuestionModel,
    ExamDescribeQuestionModel,
    Options,
    MatchingInstructionModel,
    MatchingPosibleAnswersModels,
    MatchingQuestionModel,
)
from .serializers import (
    ChoiceQuestionSerializers,
    BlankQuestionSerializers,
    DescribeQuestionSerializers,
    OptionSerializers,
    MatchingInstructionSerializers,
    MatchingPosibleAnswersSerializers,
    MatchingQuestionSerializers,
)


class MatchingInstructionList(generics.ListCreateAPIView):
    queryset = MatchingInstructionModel.objects.all()
    serializer_class = MatchingInstructionSerializers


class MatchingQuestionList(generics.ListCreateAPIView):
    queryset = MatchingQuestionModel.objects.all()
    serializer_class = MatchingQuestionSerializers


class MatchingPosibleAnswerList(generics.ListCreateAPIView):
    queryset = MatchingPosibleAnswersModels.objects.all()
    serializer_class = MatchingPosibleAnswersSerializers


class OptionList(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionSerializers


class OptionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionSerializers
    lookup_field = "id"

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class ChoiceQuestionList(generics.ListCreateAPIView):
    queryset = ExamChoiceQuestionModel.objects.all()
    serializer_class = ChoiceQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #


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
    queryset = ExamDescribeQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return self.queryset.filter(language=1)


class DescribeQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExamDescribeQuestionModel.objects.all()
    serializer_class = DescribeQuestionSerializers
    lookup_field = "questionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, questionId=None):
        return self.retrieve(request, questionId)

    def put(self, request, questionId=None):
        return self.partial_update(request, questionId)

    def delete(self, request, questionId=None):
        return self.destroy(request, questionId)

