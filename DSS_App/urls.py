from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', home,name='home'),
	path('customer_profile/<int:pk>',customer_profile,name='customer_profile'),
]
