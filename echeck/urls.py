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
from cashier.views import HomeView, CashierView, add_to_order
from storage.views import StorageView, ProductCreate, RefillToRepository, AddToRepository


urlpatterns = [


	#e_check urls
    url(r'^$', HomeView.as_view(), name='home'),


    #cashier urls
    url(r'^cashier/$', CashierView.as_view(), name='cashier'),
    

    #storage urls
    url(r'^storage/$', StorageView.as_view(), name='storage'),
    url(r'^storage/add_product/$', ProductCreate.as_view(), name='add_product'),
    url(r'^storage/refill_to_repository/(?P<pk>\d+)/$', RefillToRepository.as_view(), name='refill_to_repository'),
    url(r'^storage/add_to_repository/$', AddToRepository.as_view(), name='add_to_repository'),
	#url(r'^cashier/$', cashier, name = 'cashier'),
    url(r'^cashier/(?P<dish_id>\d+)/$', add_to_order, name = 'add_dish_to_order'),


    
    url(r'^admin/', admin.site.urls),
]
