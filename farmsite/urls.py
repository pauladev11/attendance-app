"""farmsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include(('employee.urls', 'employee'), namespace='employee')),
    path('attendance/', include(('attendance.urls', 'attendance'), namespace='attendance')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('item/', include(('item.urls', 'item'), namespace='item')),
    #path('sale/', include(('sale.urls', 'sale'), namespace='sale')),
    #path('expense/', include(('expense.urls', 'expense'), namespace='expense')),
    #path('order/', include(('order.urls', 'order'), namespace='order')),
    #path('cashflow/', include(('cashflow.urls', 'cashflow'), namespace='cashflow'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
