from .models import User
from .permissions import IsTheAllowedUser
from .serializers import UserSerializer
from rest_framework import generics,permissions

class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTheAllowedUser]