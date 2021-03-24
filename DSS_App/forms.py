from .models import *
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['data_1','data_2']