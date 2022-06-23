# dashboard/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Dashboard,Card, DataRecord
from django.contrib.auth.decorators import login_required
from channels.exceptions import AcceptConnection

#https://channels.readthedocs.io/en/latest/tutorial/part_2.html


class DashboardConsumer(WebsocketConsumer):

    
    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"ds_{self.room_id}"
        self.user = self.scope['user']
        self.machine = self.scope['machine']

        print(self.user,self.machine)

        if self.user:
            if self.user.is_anonymous:
                return None
                    
            if Dashboard.objects.filter(dshbd_users=self.user,id=self.room_id).first():
            
                async_to_sync(self.channel_layer.group_add)(
                            self.room_group_name,
                            self.channel_name
                        )
                        
                self.accept()

        if self.machine:
            self.accept()

    def disconnect(self, close_code):
        
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        new_data_record = DataRecord(linked_dshbd_id=int(self.room_id),
                    metric_name=text_data_json["metric_name"],
                    metric_value=text_data_json["value"],
                    metric_date=text_data_json["date"],
                    usersource=self.machine)       
        new_data_record.save()
        print("eer",text_data_json)
        #Send message to the group         
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,
        {   
            "type":"update",
            "metric_name":text_data_json["metric_name"],
            "metric_value":text_data_json["value"],
            "metric_date":text_data_json["date"],
        }
        )
    
 
    def update(self,event):

        self.send(text_data=json.dumps(event))