from datasocks.models import Dashboard
from rest_framework import serializers


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = "__all__"