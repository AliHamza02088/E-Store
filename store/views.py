import re
from unicodedata import category
from django.shortcuts import render
from .models import *

# Create your views here.
def index_view(request):
    trending_items = Product.objects.all()[:8]
    subcategory_filter = request.GET.get('subcategory')
    if subcategory_filter:
        mobile_phones = Product.objects.filter(
            category__name='mobile_phone',
            subcategory__name=subcategory_filter
        )[:6]
    else:
        mobile_phones = Product.objects.filter(category__name='mobile_phone')[:6]
    
    if subcategory_filter:
        tablets = Product.objects.filter(
            category__name='tablet',
            subcategory__name=subcategory_filter
        )[:6]
    else:
        tablets = Product.objects.filter(category__name='tablet')[:6]

    context = {
        'trending_items': trending_items, 
        'mobile_phones': mobile_phones, 
        'tablets': tablets,
        'sub_categories': SubCategory.objects.all(),
        'selected_subcategory': subcategory_filter,
    }
    return render(request, 'index.html', context)

def product_view(request):
    subcategory_filter = request.GET.get('subcategory')
    products = Product.objects.all()
    if subcategory_filter:
        products = products.filter(subcategory__name=subcategory_filter)
    
    context = {
        'products': products,
        'sub_categories': SubCategory.objects.all(),
        'selected_subcategory': subcategory_filter,
    }
    return render(request, 'product.html', context)

def product_details_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})
