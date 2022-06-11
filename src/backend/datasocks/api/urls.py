from django.urls import path
from django.conf import settings
from .views import DashboardViewSet
from rest_framework import routers

app_name = "datasocks"

router = routers.SimpleRouter()
router.register(r"dashboards", DashboardViewSet,basename="dashboards") 
urlpatterns = router.urls