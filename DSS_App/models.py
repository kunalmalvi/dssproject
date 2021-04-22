from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
	user 		= 	models.ForeignKey(User, on_delete=models.CASCADE)
	acc_number	=	models.IntegerField(null=False,unique=True)
	c_id		=	models.AutoField(primary_key=True)
	first_name 	= 	models.CharField(max_length=100, blank=False)
	last_name 	= 	models.CharField(max_length=100, blank=False)
	email           =	models.EmailField(max_length=50,unique=True,blank=False)
	phone	        =	models.IntegerField(null=True)
	balance 	=	models.FloatField(null=False,blank=False)

	def __str__(self):
		return self.first_name+" "+self.last_name

	def get_absolute_url(self):
		return reverse('customer_profile', kwargs={'pk': self.pk})

class Transactions(models.Model):
	t_id		=	models.AutoField(primary_key=True)
	sender_acc	=	models.IntegerField(null=False)
	receiver_acc	=	models.IntegerField(null=False)
	transactions_amount		=		models.FloatField(null=False,blank=False)
	transaction_time = models.DateTimeField(auto_now_add=True)
