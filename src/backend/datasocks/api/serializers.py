from datasocks.models import Dashboard,Button,Card,DataRecord,Graph
from rest_framework import serializers

class ButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Button
        fields = "__all__"


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class GraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Graph
        fields = ["id","linked_dshbd","first_data_serie","second_data_serie","graph_color","graph_name","graph_type"]


class DashboardSerializer(serializers.ModelSerializer):
    button = ButtonSerializer(many=True,read_only=True)
    card = CardSerializer(many=True,read_only=True)
    graph = GraphSerializer(many=True,read_only=True)
    
    class Meta:
        model = Dashboard
        fields = ["id","dshbd_name","dshbd_description","dshbd_users","button","card","graph"]



class DataRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DataRecord
        fields = "__all__"