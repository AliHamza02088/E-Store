from django.contrib import admin
from .models import Product , Category , SubCategory

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'avaliabilty', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('avaliabilty', 'created_at')

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(SubCategory, SubCategoryAdmin)