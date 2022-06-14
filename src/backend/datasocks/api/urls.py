from django.urls import path
from django.conf import settings
from .views import DashboardViewSet,ButtonViewSet,CardViewSet,DataRecordsAPI
from rest_framework import routers

app_name = "datasocks"

router = routers.SimpleRouter()
router.register(r"dashboards", DashboardViewSet,basename="dashboards")
router.register(r"buttons", ButtonViewSet,basename="buttons")
router.register(r"cards", CardViewSet,basename="cards")
urlpatterns = [
    path('data/', DataRecordsAPI.as_view()),
]

 
urlpatterns += router.urls