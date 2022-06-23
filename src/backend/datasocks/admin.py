from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from .models import Dashboard,Button,Card,DataRecord,Graph,Machine,MachineAccessAPIKey
# Register your models here.
@admin.register(MachineAccessAPIKey)
class ClientAPIKeyModelAdmin(APIKeyModelAdmin):
    pass


admin.site.register(Dashboard)
admin.site.register(Button)
admin.site.register(Card)
admin.site.register(DataRecord)
admin.site.register(Graph)
admin.site.register(Machine)