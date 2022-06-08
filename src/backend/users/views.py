from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from . import serializers
from .users_utils import get_and_authenticate_user, create_user_account

User = get_user_model()


class UserViewSet(viewsets.GenericViewSet):
    def create(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):

        if self.action == "create":
            return serializers.UserRegisterSerializer

        if self.action == "retrieve" or self.action == "list":
            return serializers.UserSerializer

        if self.action == "update":
            return serializers.PasswordChangeSerializer

        return serializers.EmptySerializer

    def get_queryset(self):

        if self.request.user.is_staff or self.request.user.is_superuser:
            return User.objects.all()

        elif self.request.user.is_authenticated:
            return User.objects.filter(id=self.request.user.id)
        else:
            return User.objects.none()


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [
        AllowAny,
    ]  # Allow Any -> Permet a n'importe qui de se log

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def login(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def logout(self, request):
        self.request.user.auth_token.delete()
        logout(request)
        data = {"success": "Sucessfully logged out"}
        return Response(data=data, status=status.HTTP_200_OK)

    def get_serializer_class(self):

        if self.action == "login":
            return serializers.UserLoginSerializer

        return serializers.EmptySerializer
