from django.urls import path
from . import views
from .views import *


urlpatterns = [
	path('', home,name='home'),
	path('student_profile/<int:pk>',student_profile,name='student_profile'),
]
