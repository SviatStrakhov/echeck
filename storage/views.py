from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Repository, Product
from .forms import ProductForm, RepositoryForm


class StorageView(ListView):

	 template_name = 'storage/storage.html'
	 queryset = Repository.objects.all()



class ProductCreate(CreateView):
	model = Product
	template_name = 'storage/add_product.html'
	fields = ['title', 'cost', 'unit', 'category']
	success_url = '/storage'

	# def form_valid(self, form):
	# 	errors = {}
	# 	data = Product.objects.all()
	# 	title = request.POST.get('title').strip()
	# 	if title in data:
	# 		errors['title'] = 'Product already exist!'
	# 	if not errors:
	# 		form.save()
	# 		return redirect(self.get_success_url())





class RefillToRepository(UpdateView):
	model = Repository
	template_name = 'storage/add_to_repository.html'
	fields = ['title', 'balance']
	success_url = '/storage'





# def add_product(request):

# 	if request.method == 'POST':
# 		form = ProductForm(request.POST)

# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect(reverse('storage'))

# 	else:
# 		form = ProductForm()
# 	return render(request, 'storage/add_product.html', {'form': form})

# def add_to_repository(request, pk):

# 	product = Repository.objects.get(id=pk)
# 	if request.method == 'POST':
# 		form = RepositoryForm(request.POST, instance=product)

# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect(reverse('storage'))

# 	else:
# 		form = RepositoryForm()
# 	return render(request, 'storage/add_to_repository.html', {'form': form})