from django.shortcuts import render
from rest_framework import generics
from models_app.models import (
    G_ChoiceQuestionModel,
    G_Options,
    G_UnitModel,
    GeneralKnowlegdyModel,
)


from .serializers import (
    GeneralKnowledySerializers,
    G_ChoiceQuestionSerializers,
    G_OptionsSerializers,
    G_UnitSerializers,
)


class GeneralKnowledgyList(generics.ListCreateAPIView):
    queryset = GeneralKnowlegdyModel.objects.all()
    serializer_class = GeneralKnowledySerializers
    # permission_classes = (permissions.IsAuthenticated,)


class GeneralKnowledgyRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralKnowlegdyModel.objects.all()
    serializer_class = GeneralKnowledySerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class G_ChoiceQuestionList(generics.ListCreateAPIView):
    queryset = GeneralKnowlegdyModel.objects.all()
    serializer_class = G_ChoiceQuestionSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class G_ChoiceQuestionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralKnowlegdyModel.objects.all()
    serializer_class = G_ChoiceQuestionSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class G_OptionsList(generics.ListCreateAPIView):
    queryset = G_Options.objects.all()
    serializer_class = G_OptionsSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class G_OptionsRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = G_Options.objects.all()
    serializer_class = G_OptionsSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class G_UnitList(generics.ListCreateAPIView):
    queryset = G_UnitModel.objects.all()
    serializer_class = G_UnitSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class G_UnitRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = G_UnitModel.objects.all()
    serializer_class = G_UnitSerializers
    lookup_field = "id"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
