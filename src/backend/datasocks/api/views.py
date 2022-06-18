from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from datasocks.models import Dashboard, Button, Card, DataRecord, Graph
from .serializers import DashboardSerializer, ButtonSerializer, CardSerializer, DataRecordSerializer, GraphSerializer
from rest_framework.response import Response
from itertools import chain

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

class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer
    
    def get_queryset(self):

        user = self.request.user
        dashboard_qs = Dashboard.objects.filter(dshbd_users=user)

        # TODO : Refactor this
        if self.kwargs.get('pk'):

            card =  Card.objects.filter(pk=self.kwargs['pk']).first()
            
            dashboard = Dashboard.objects.filter(id=card.linked_dshbd_id).first()

            if user in dashboard.dshbd_users.all():
                return Card.objects.filter(pk=self.kwargs['pk'])
            
            return Card.objects.none()
        
        cards_qs_list = [Card.objects.filter(linked_dshbd=dashboard) for dashboard in dashboard_qs]
        
        return chain(*cards_qs_list)


class DataRecordsAPI(generics.ListCreateAPIView):
    queryset = DataRecord.objects.none()
    serializer_class = DataRecordSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        dashboard_id = request.query_params["dashboard"]
        metric_name = request.query_params["metric"]
        last = request.query_params["last"]

        if last=="True":
            queryset = DataRecord.objects.filter(linked_dshbd_id=dashboard_id,metric_name=metric_name).order_by('-metric_date')[0]
            serializer = DataRecordSerializer(queryset, many=False)

            
        else:
            queryset = DataRecord.objects.filter(metric_name=metric_name,linked_dshbd_id=dashboard_id).order_by("metric_date")
        
            serializer = DataRecordSerializer(queryset, many=True)
        return Response(serializer.data)


class GraphViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GraphSerializer
    
    def get_queryset(self):
        return Graph.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        print(data)
        data['created_by'] = request.user

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)