from rest_framework import generics, permissions
from models_app.models import UnitModel
from .serializers import UnitSerializers


class UnitList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = UnitModel.objects.all()
    serializer_class = UnitSerializers


class UnitRUD(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = UnitModel.objects.all()
    serializer_class = UnitSerializers
    lookup_field = "unitId"

    def get(self, request, unitId=None):
        return self.retrieve(request, unitId)

    def put(self, request, unitId=None):
        return self.partial_update(request, unitId)

    def delete(self, request, unitId=None):
        return self.destroy(request, unitId)
