from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', home,name='home'),
	path('customer_profile',customer_profile,name='customer_profile'),
	path('fund_transfer',fund_transfer,name='fund_transfer'),
]
