from users.models import User
from .serializers import UserRegisterSerializer
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from knox.auth import AuthToken

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model_serializer = UserRegisterSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=model_serializer.data['username'], email=model_serializer.data['email'], password=model_serializer.data['password'], bio=model_serializer.data['bio'])
        _, knox_token = AuthToken.objects.create(user)
        return Response({"token": knox_token, "user": {"id": user.id, "username": user.username, "email": user.email, "bio": user.bio}}, status=201)


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthTokenSerializer

    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, knox_token = AuthToken.objects.create(user)
        return Response({"token": knox_token, "user": {"id": user.id, "username": user.username, "email": user.email, "bio": user.bio}}, status=200)
