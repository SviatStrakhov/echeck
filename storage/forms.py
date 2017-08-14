from django.forms import ModelForm
from .models import Product, Repository


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'cost', 'unit', 'category']


class RepositoryForm(ModelForm):

    class Meta:
        model = Repository
        fields = ['title', 'balance']
