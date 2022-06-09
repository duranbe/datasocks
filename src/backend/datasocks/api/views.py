from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from datasocks.models import Dashboard
from .serializers import DashboardSerializer

class DashboardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return Dashboard.objects.filter(dshbd_users=self.request.user.id)