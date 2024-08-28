from django.urls import path
from apps.views import *

urlpatterns = [
	path('', Index, name='home'),
]