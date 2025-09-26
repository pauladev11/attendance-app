from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employee, name='list_employee'),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('create_employee', views.create_employee, name='create_employee'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]	
