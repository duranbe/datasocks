from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from rest_framework.response import Response

app_name = "users"

from .views import AuthViewSet, UserViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register("auth", AuthViewSet, basename="auth")  # Auth urls (login/logout)
router.register("user", UserViewSet, basename="user")  # User CRUD urls
urlpatterns = router.urls
