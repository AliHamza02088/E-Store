from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('product/', product_view, name='product'),
    path('product-detail/<int:product_id>/', product_details_view, name='product_detail'),
]
