from django.shortcuts import render
from rest_framework import generics
from models_app.models import (
    LearnLanguageModel,
    L_ChoiceQuestionModel,
    L_Options,
    L_UnitModel,
)

from .serializers import (
    LearnLanguageSerializers,
    L_ChoiceQuestionSerializers,
    L_OptionsSerializers,
    L_UnitSerializers,
)


class LearnLanguageList(generics.ListCreateAPIView):
    queryset = LearnLanguageModel.objects.all()
    serializer_class = LearnLanguageSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class LearnLanguageRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = LearnLanguageModel.objects.all()
    serializer_class = LearnLanguageSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class L_ChoiceQuestionList(generics.ListCreateAPIView):
    queryset = L_ChoiceQuestionModel.objects.all()
    serializer_class = L_ChoiceQuestionSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class L_ChoiceQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = L_ChoiceQuestionModel.objects.all()
    serializer_class = L_ChoiceQuestionSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class L_OptionsList(generics.ListCreateAPIView):
    queryset = L_Options.objects.all()
    serializer_class = L_OptionsSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class L_OptionsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = L_Options.objects.all()
    serializer_class = L_OptionsSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class L_UnitList(generics.ListCreateAPIView):
    queryset = L_UnitModel.objects.all()
    serializer_class = L_UnitSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class L_UnitRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = L_UnitModel.objects.all()
    serializer_class = L_UnitSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
