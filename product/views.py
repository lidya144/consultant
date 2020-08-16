from rest_framework import generics, permissions
from models_app.models import Contactinfo
from .serializers import ContactSerializer


class ContactinfoList(generics.ListCreateAPIView):
    queryset = Contactinfo.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ContactinfoRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contactinfo.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "id"
    # permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

