from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Test(models.Model):
	data_1		=	models.CharField(max_length=40,blank=False)
	data_2		=	models.CharField(max_length=40,blank=False)