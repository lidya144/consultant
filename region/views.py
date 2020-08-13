from rest_framework import generics, permissions
from models_app.models import RegionModel
from .serializers import RegionSerializers


class RegionList(generics.ListCreateAPIView):
    queryset = RegionModel.objects.all()
    serializer_class = RegionSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class RegionRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = RegionModel.objects.all()
    serializer_class = RegionSerializers
    lookup_field = "id"
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

