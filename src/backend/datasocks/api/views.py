from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
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
        serializer = DashboardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Dashboard.objects.filter(dshbd_users=self.request.user.id,pk=pk).first()
        serializer = DashboardSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Dashboard.objects.filter(dshbd_users=self.request.user.id,pk=pk).first()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


