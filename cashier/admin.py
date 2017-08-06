#admin
from django.contrib import admin
from .models import *
from kitchen.models import DishComposition
 

 
class DishInline (admin.TabularInline):
	model = Dish

class DishCategoryAdmin (admin.ModelAdmin):
	inlines = (DishInline, )


class MenuCompositionInline (admin.TabularInline):
	model = MenuComposition

class MenuAdmin (admin.ModelAdmin):
	inlines = (MenuCompositionInline, )


class OrderCompositionInline (admin.TabularInline):
	model = OrderComposition

class OrderAdmin (admin.ModelAdmin):
	inlines = (OrderCompositionInline, )


class DishCompositionInline (admin.TabularInline):
	model = DishComposition

class DishAdmin (admin.ModelAdmin):
	inlines = (DishCompositionInline, )





# Register your models here.
admin.site.register(Dish, DishAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(CategoryDish, DishCategoryAdmin)
admin.site.register(MenuComposition)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderComposition)



