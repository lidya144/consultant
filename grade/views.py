from django.shortcuts import render
from rest_framework import generics
from models_app.models import GradeModel
from .serializers import GradeSerializers


class GradeList(generics.ListCreateAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializers

    # permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #    return self.queryset.filter(language=1)


class GradeRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializers
    lookup_field = "gradeId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, gradeId=None):
        return self.retrieve(request, gradeId)

    def put(self, request, gradeId=None):
        return self.partial_update(request, gradeId)

    def delete(self, request, gradeId=None):
        return self.destroy(request, gradeId)

