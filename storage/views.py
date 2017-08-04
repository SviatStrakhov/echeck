from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Repository



class StorageView(ListView):

	 template_name = 'storage/storage.html'
	 queryset = Repository.objects.all()