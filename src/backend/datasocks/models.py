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

