from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.home, name='home'),
    path('register_attendance/', views.register_attendance, name='register_attendance'),
    path('time-in/', views.time_in, name='time_in'),
    path('time-out/', views.time_out, name='time_out'),
    path('attendance-record/', views.attendance_record, name='attendance_record'),
    
]

