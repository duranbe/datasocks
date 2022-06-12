from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core import serializers
from datetime import datetime
from django.contrib.postgres.fields import JSONField
from django.core.validators import RegexValidator

User = settings.AUTH_USER_MODEL 

class Dashboard(models.Model):
	dshbd_name = models.CharField(max_length=30,verbose_name='Dashboard Name')
	dshbd_description = models.CharField(max_length=100,verbose_name='Dashboard Description')
	dshbd_users = models.ManyToManyField(User,verbose_name='Dashboard Allowed Users')
	
	class Meta:
		ordering = ['dshbd_name']
		verbose_name = "Dashboard"
		
	def get_user(self):
		return(self.dshbd_users)

	def __str__(self):
		return self.dshbd_name


class Button(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="button")
	btn_action = models.CharField(max_length=50,verbose_name='Button Action')
	btn_title = models.CharField(max_length=20,verbose_name='Button Title')
	btn_description = models.CharField(max_length=150,verbose_name='Button Description')

	class Meta:
		verbose_name = "Button"

	def __str__(self):
		return self.btn_title

class Card(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="card")
	card_name = models.CharField(max_length=50,verbose_name='Card Name')
	card_description = models.CharField(max_length=150,verbose_name='Card Description')
	card_date = models.DateTimeField(auto_now=True)
	
	class Meta():
		verbose_name ="Card"

	def __str__(self):
		return self.card_name
 

class DataRecord(models.Model):
	linked_dshbd = models.ForeignKey(Dashboard,on_delete=models.CASCADE,related_name="datarecord")
	metric_name = models.CharField(max_length=100,verbose_name="Metric Name")
	metric_value = models.FloatField()
	metric_date = models.DateTimeField(auto_now_add=True,blank=False)
	saved_datetime = models.DateTimeField(auto_now_add=True)
	usersource = models.ForeignKey(User,on_delete=models.PROTECT,related_name="datarecord")

