from django.urls import path
from django.conf import settings
from .views import DashboardViewSet
from rest_framework import routers

app_name = "datasocks"

router = routers.DefaultRouter(trailing_slash=False)
router.register("api/1/dashboards/", DashboardViewSet, basename="datasocks") 
urlpatterns = router.urls