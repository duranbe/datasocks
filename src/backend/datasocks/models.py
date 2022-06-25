from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core import serializers
from datetime import datetime
from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator
from rest_framework_api_key.models import AbstractAPIKey

User = settings.AUTH_USER_MODEL 

class Dashboard(models.Model):
	dshbd_name = models.CharField(max_length=30,verbose_name='Dashboard Name',unique=True)
	dshbd_description = models.CharField(max_length=100,verbose_name='Dashboard Description',unique=True)
	dshbd_users = models.ManyToManyField(User,verbose_name='Dashboard Allowed Users')
	
	class Meta:
		ordering = ['id']
		verbose_name = "Dashboard"
		
	def get_user(self):
		return(self.dshbd_users)

	def __str__(self):
		return self.dshbd_name


class Button(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="button")
	btn_action = models.CharField(max_length=50,verbose_name='Button Action',unique=True)
	btn_title = models.CharField(max_length=20,verbose_name='Button Title',unique=True)
	btn_description = models.CharField(max_length=150,verbose_name='Button Description',unique=True)

	class Meta:
		verbose_name = "Button"

	def __str__(self):
		return self.btn_title

	
		

class Card(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="card")
	card_name = models.CharField(max_length=50,verbose_name='Card Name',unique=True)
	card_description = models.CharField(max_length=150,verbose_name='Card Description',unique=True)
	card_date = models.DateTimeField(auto_now=True)
	
	class Meta():
		verbose_name ="Card"

	def __str__(self):
		return self.card_name
 
	def has_user_rights(self,user):
		dashboard = Dashboard.objects.filter(pk=self.linked_dshbd).first()

		return(user in dashboard.dshbd_users.all())


	@property 
	def user_permissions(self):
		dashboard = Dashboard.objects.filter(pk=self.linked_dshbd).first()
		return dashboard.dshbd_users.all()

class Machine(models.Model):
	machine_name = models.CharField(max_length=128,blank=False,null=False,unique=True)
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="machine")
	

	def __str__(self):
		return self.machine_name

class MachineAccessAPIKey(AbstractAPIKey):
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="api_key",
    )

    class Meta:
       verbose_name ="Machine Access API Key"
		
class DataRecord(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="datarecord")
	metric_name = models.CharField(max_length=100,verbose_name="Metric Name")
	metric_value = models.FloatField()
	metric_date = models.DateTimeField(auto_now_add=True,blank=False)
	saved_datetime = models.DateTimeField(auto_now_add=True)
	usersource = models.ForeignKey(Machine,on_delete=models.PROTECT,related_name="datarecord")


class Graph(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="graph")
	first_data_serie = models.CharField(max_length=50,verbose_name='first_data_series',null=False)
	second_data_serie = models.CharField(max_length=50,verbose_name='second_data_serie',null=True,blank=True)
	graph_color=models.CharField(max_length=7,verbose_name='line_color',default="#f0a860")
	graph_name = models.CharField(max_length=50,verbose_name='Graph Name',unique=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	
	choices = [
	('LN','Line Plot'),
	('AR','Area Chart'),
	('BR','Bar Plot'),
	('RD','Radar Plot'),
	('PI','Pie Plot'),
	('BL','Bubble Plot'),
	('ST','Scatter Plot')
	]

	graph_type=models.CharField(max_length=2,choices=choices,default=None)

	def __str__(self):
		return(self.graph_name)

