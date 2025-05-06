from django.urls import path
from .views import home

app_name = 'schedules'

urlpatterns = [
  path('', home, name='home'),
]