from django.db import models


class CategoryProduct(models.Model):

	class Meta(object):
		verbose_name = 'Category'
		verbose_name_plural = 'Category'

	title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title')

	def __str__(self):
		return f'{self.title}'



class Product(models.Model):

	class Meta(object):
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title')

	cost = models.DecimalField(
		blank=False,
		max_digits=6,
        decimal_places=2,
        verbose_name='cost')

	unit = models.CharField(
		max_length=256,
    	blank=False,
    	verbose_name='unit')

	category = models.ForeignKey(CategoryProduct,
    	blank=True,
    	null=True,
    	on_delete=models.SET_NULL)

	def __str__(self):
		return f'{self.title}'


class Repository(models.Model):

	class Meta(object):
		verbose_name = 'Repository'
		verbose_name_plural = 'Repository'


	product = models.ForeignKey(Product,
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	balance = models.DecimalField(
		blank=False,
		max_digits=6,
        decimal_places=2,
        verbose_name='balance')

	def __str__(self):
		return f'{self.product}'