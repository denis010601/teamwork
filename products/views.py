from django.shortcuts import render
from django.views.generic import ListView

from products.models import Products


class ProductListView(ListView):
    model = Products
    # template_name = 'products/products_list.html'
