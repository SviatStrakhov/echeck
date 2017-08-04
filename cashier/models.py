from django.db import models
 
 
# Create your models here.
 
 
class CategoryDish (models.Model):
 
    class Meta(object):
        verbose_name = 'category'
        verbose_name_plural = 'category'

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title')
 
    def __str__(self):
        return f'{self.title}'
 
 
 
class Dish (models.Model):
 
 
    class Meta(object):
        verbose_name = 'Dish'
        verbose_name_plural = 'Dish'
 
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='title')
 
    cost = models.DecimalField (
        blank=False,
        max_digits=6,
        decimal_places=2,
        verbose_name='cost')
 
    price = models.DecimalField(
        blank=True,
        max_digits=7,
        decimal_places=2,
        verbose_name='price')
 
    category = models.ForeignKey(CategoryDish,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
 
 
 
 
    def __str__(self):
        return '{}'.format(self.title)
 
 
 
class MenuComposition (models.Model):
 
 
    class Meta(object):
        verbose_name = 'MenuComposition'
        verbose_name_plural = 'MenuComposition'
 
 
    dish = models.ForeignKey(Dish,
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
 
    menu = models.ForeignKey('Menu',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
 
    quantity = models.DecimalField(
        blank=True,
        max_digits=7,
        decimal_places=1,
        verbose_name='quantity')
 
 
class Menu (models.Model):
 
 
    class Meta(object):
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
 
 
 
    date = models.DateField(
        blank=True)
 
 
    def __str__(self):
        return '{}'.format(self.date)
 
 
class Order (models.Model):
 
    class Meta(object):
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
        

    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True)

    
 
 
 
    def __str__(self):
        return '{}'.format(self.date)


class OrderComposition (models.Model):

    class Meta(object):
        verbose_name = 'OrderComposition'
        verbose_name_plural = 'OrderComposition'

    dish = models.ForeignKey(Dish,
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    order = models.ForeignKey(Order,
        blank=False,
        null=True,
        on_delete=models.SET_NULL)

    quantity = models.DecimalField(
        blank=True,
        max_digits=7,
        decimal_places=1,
        verbose_name='quantity')
