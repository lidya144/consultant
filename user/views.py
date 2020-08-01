from rest_framework import authentication, generics, permissions, status
from rest_framework.response import Response
from .serializers import (
    LoginSerializer,
    UserSerializer,
)
from models_app.models import User


class SignupUserView(generics.ListCreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(user)

    def get(self, request):
        return self.list(request)


class UpdateDeleteUserView(generics.RetrieveUpdateDestroyAPIView):
    """Update, Delete signup user info"""

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


class LoginAPIView(generics.CreateAPIView):
    """Login users with valid credintials"""

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return serializer.validated_data

