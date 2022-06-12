from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import status
from datasocks.models import Dashboard, Button, Card
from .serializers import DashboardSerializer, ButtonSerializer, CardSerializer
from rest_framework.response import Response

class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DashboardSerializer
    queryset= Dashboard.objects.all()
    
    def list(self, request):
        queryset=Dashboard.objects.filter(dshbd_users=self.request.user.id)
        serializer = DashboardSerializer(queryset, many=True)
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


class ButtonViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ButtonSerializer
    queryset= Button.objects.all()
    
    def list(self, request):
        serializer = ButtonSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ButtonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        #queryset = Button.objects.filter(linked_dshb=self.request.user.id,pk=pk).first()
        serializer = ButtonSerializer(self.queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Button.objects.filter(linked_dshb=self.request.user.id,pk=pk).first()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer
    queryset= Card.objects.all()
    
    def list(self, request):
        print(self.request)
        print(self.request.user.id)
        print(self.request.query_params)    

        
        serializer = CardSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        #queryset = Card.objects.filter(linked_dshb=self.request.user.id,pk=pk).first()
        serializer = CardSerializer(self.queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        queryset = Card.objects.filter(linked_dshb=self.request.user.id,pk=pk).first()
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)