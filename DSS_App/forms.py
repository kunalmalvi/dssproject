from .models import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name","last_name","acc_number","email","phone","balance"]
