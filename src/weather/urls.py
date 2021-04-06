from django.urls import path
from .views import *

app_name = 'weather'

urlpatterns = [
	path('weather/', homeview, name='home'),
	path('weather/delete-city/<str:city>/', delete_cityview, name='delete'),
]