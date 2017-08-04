from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Menu, MenuComposition, Dish, OrderComposition, Order
from datetime import datetime
from django.urls import reverse
from django.views.generic import TemplateView, ListView
# Create your views here.

class HomeView(TemplateView):

	template_name = 'cashier/base.html'


class CashierView(ListView):

	template_name = 'cashier/cashier.html'
	queryset = MenuComposition.objects.all().filter(menu_id=Menu.objects.get(date=datetime.today().strftime('%Y-%m-%d')))

'''
def home(request):
	return render(request, 'cashier/base.html')

def cashier(request):
	date = datetime.today().strftime('%Y-%m-%d')
	dishes = MenuComposition.objects.all().filter(menu_id=Menu.objects.get(date=date))
	#if order_id:
	#	order = get_object_or_404(Order, id=order_id)
	#else:
	#	order = {}
	return render(request, 'cashier/cashier.html', {'dishes':dishes, 'date':date})


	, order_id=None
def add_dish_to_order(request, dish_id):
	dish = get_object_or_404(Dish, id=dish_id)


	order = Order.objects.create()
	order_comp = OrderComposition.objects.create(order=order, dish=dish, quantity=1)
	order.save()
	order_comp.save()
	next_page = request.GET.get('next', reverse('cashier', kwargs={'order_id': order.id}))

	return redirect(next_page)
'''
