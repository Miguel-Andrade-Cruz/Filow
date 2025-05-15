from django.urls import path
from .views import home, new_schedule

app_name = 'schedules'

urlpatterns = [
  path('', home, name='home'),
  path('new/', new_schedule, name='new_schedule'),
]