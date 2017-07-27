#admin
from django.contrib import admin
from .models import *
 

 
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
'''
class MenuInline (admin.TabularInline):
   model = Menu
 
class MenuAdmin (admin.ModelAdmin):
   inlines = [ MenuInline ]
'''
 
#class MenuCompositionInline (admin.TabularInline):
#model = MenuComposition
 
 
#class MenuCompositionAdmin (admin.ModelAdmin):
#    inlines = (MenuCompositionInline)
 

# Register your models here.
admin.site.register(Dish)
admin.site.register(Menu, MenuAdmin)
admin.site.register(CategoryDish, DishCategoryAdmin)
admin.site.register(MenuComposition)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderComposition)



