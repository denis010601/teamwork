from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from products.models import Products, Category


class ProductListView(ListView):
    model = Products
    template_name = 'products/products_list.html'

    def get(self, request, *args, **kwargs):
        category_str = request.GET.get('category')
        category_id = int(category_str) if category_str else 0
        categories = Category.objects.annotate(count=Count('products')).filter(count__gt=0)
        products_list = Products.objects.filter(category=category_id) if category_id else Products.objects.all()
        return render(request, template_name=self.template_name, context={'products_list': products_list,'categories': categories})

class ProductDetailView(DetailView):
    model = Products