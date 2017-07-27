"""echeck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include ,url
from django.contrib import admin
from cashier.views import cashier, add_dish_to_order

urlpatterns = [


	#e_check urls
	url(r'^cashier/(?P<order_id>[0-9]+)/$', cashier, name = 'cashier'),
    url(r'^cashier/add_to_order/(?P<dish_id>\d+)/$', add_dish_to_order, name = 'add_dish_to_order'),



    #cashier urls
    #url(r'^storage/$'),

    
    url(r'^admin/', admin.site.urls),
]
