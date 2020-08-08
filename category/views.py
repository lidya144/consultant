from django.shortcuts import render
from rest_framework import generics
from models_app.models import CategoryModel
from .serializers import CategorySerializers


class CategoryList(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers

    def get_queryset(self):
        return self.queryset.all()


class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializers
    lookup_field = "categorytId"

    def get(self, request, categorytId=None):
        return self.retrieve(request, categorytId)

    def put(self, request, categorytId=None):
        return self.partial_update(request, categorytId)

    def delete(self, request, categorytId=None):
        return self.destroy(request, categorytId)

