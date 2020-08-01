from django.shortcuts import render
from rest_framework import generics
from models_app.models import TransactionModel
from .serializers import TransactionSerializers


class TransactionList(generics.ListCreateAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializers

    # permission_classes = (permissions.IsAuthenticated,)


class TransactionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionSerializers
    lookup_field = "transactionId"

    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, transactionId=None):
        return self.retrieve(request, transactionId)

    def put(self, request, transactionId=None):
        return self.partial_update(request, transactionId)

    def delete(self, request, transactionId=None):
        return self.destroy(request, transactionId)

