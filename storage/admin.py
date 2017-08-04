from django.contrib import admin
from .models import *

# Register your models here.

'''
class ProductInline(admin.TabularInline):
	model = Product

class ProductCategoryAdmin(admin.ModelAdmin):
	inlines = (ProductInline, )
'''


admin.site.register(Product)
admin.site.register(CategoryProduct)
admin.site.register(Repository)
#admin.site.register()