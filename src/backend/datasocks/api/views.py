from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from datasocks.models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.response import Response

class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DashboardSerializer
    queryset= Dashboard.objects.all()
    
    def list(self, request):
        queryset=Dashboard.objects.filter(dshbd_users=self.request.user.id)
        serializer = DashboardSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = Dashboard.objects.filter(dshbd_users=self.request.user.id,pk=pk).first()
        serializer = DashboardSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


