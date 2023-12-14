from django.shortcuts import render
from django.views.generic import DetailView, ListView

from products.models import Products


class NewsView(ListView):
    model = Products
    fields = '__all__'
    template_name = 'product.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Products.objects.all()

class NewsListView(ListView):
    model = Products
    template_name = 'product_list.html'

class NewsDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'

    def get_queryset(self):
        return Products.objects.all()
