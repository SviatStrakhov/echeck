from django.db import models
from storage.models import Product
from cashier.models import Dish
# Create your models here.


class Ingredient(models.Model):

	class Meta(object):

		verbose_name = 'Ingredient'
		verbose_name_plural = 'Ingredients'

	title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title')

	product = models.ForeignKey(Product,
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	unit = models.CharField(
		max_length=256,
    	blank=False,
    	verbose_name='unit')

	cost = models.DecimalField(
		blank=False,
		max_digits=6,
        decimal_places=2,
        verbose_name='cost')

	def __str__(self):
		return f'{self.title}'


class DishComposition(models.Model):


	class Meta(object):

		verbose_name = 'Dishcomposition'
		verbose_name_plural = 'Dishcomposition'


	ingredient = models.ForeignKey(Ingredient,
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	quantity = models.DecimalField(
        blank=True,
        max_digits=7,
        decimal_places=1,
        verbose_name='quantity')

	dish = models.ForeignKey(Dish,
		blank=True,
		null=True,
		on_delete=models.SET_NULL)


