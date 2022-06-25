from datasocks.models import (
    Dashboard,
    Button,
    Card,
    DataRecord,
    Graph,
    Machine,
    MachineAccessAPIKey,
)
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
        fields = [
            "id",
            "linked_dshbd",
            "first_data_serie",
            "graph_color",
            "graph_name",
            "graph_type",
        ]


class MachineAccessAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineAccessAPIKey
        fields = ["prefix"]


class MachineSerializer(serializers.ModelSerializer):

    api_key = MachineAccessAPIKeySerializer(many=False, read_only=True)

    class Meta:
        model = Machine
        fields = ["machine_name", "linked_dshbd", "api_key"]


class DashboardSerializer(serializers.ModelSerializer):
    button = ButtonSerializer(many=True, read_only=True)
    card = CardSerializer(many=True, read_only=True)
    graph = GraphSerializer(many=True, read_only=True)
    machine = MachineSerializer(many=True, read_only=True)

    class Meta:
        model = Dashboard
        fields = [
            "id",
            "dshbd_name",
            "dshbd_description",
            "button",
            "card",
            "graph",
            "machine",
        ]


class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = "__all__"
