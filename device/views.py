from rest_framework import generics, permissions
from models_app.models import DeviceModel
from .serializers import DeviceSerializers


class DeviceList(generics.ListCreateAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializers
    # permission_classes = (permissions.IsAuthenticated,)


class DeviceRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializers
    lookup_field = "id"
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

