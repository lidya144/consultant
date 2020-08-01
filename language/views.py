from rest_framework import generics, permissions
from models_app.models import LanguageModel
from .serializers import LanguageSerializers


class LanguageList(generics.ListCreateAPIView):
    """
    This is the class where languages are manupulated
    """

    # permission_classes = (permissions.IsAuthenticated,)

    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializers


class LanguageRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    This is the class where languages are manupulated
    """

    permission_classes = (permissions.IsAuthenticated,)

    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializers
    lookup_field = "languageId"

    def get(self, request, languageId=None):
        return self.retrieve(request, languageId)

    def put(self, request, languageId=None):
        return self.partial_update(request, languageId)

    def delete(self, request, languageId=None):
        return self.destroy(request, languageId)

