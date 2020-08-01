from django.shortcuts import render
from rest_framework import generics, permissions
from models_app.models import SubjectModel
from .serializers import SubjectSerializers


class SubjectList(generics.ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class SubjectRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializers
    lookup_field = "subjectId"
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, subjectId=None):
        return self.retrieve(request, subjectId)

    def put(self, request, subjectId=None):
        return self.partial_update(request, subjectId)

    def delete(self, request, subjectId=None):
        return self.destroy(request, subjectId)

