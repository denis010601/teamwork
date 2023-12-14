from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from products.models import Products, Category


class ProductListView(ListView):
    # model = Products
    template_name = 'products/products_list.html'

    def post(self, request, *args, **kwargs):
        category_str = request.POST.get('category')
        if category_str:
            category_id = int(category_str)
        else:
            category_id = 0
        if category_id > 0:
            products_list = Products.objects.filter(category=category_id)
            msg = f"Это фильтр категория {category_id}"

        else:
            products_list = Products.objects.all()
            msg = f"Это просто страница {category_id}"
        categories = Category.objects.all()
        return render(request, template_name=self.template_name,
                      context={'products_list': products_list, 'msg': msg, 'categories': categories})

    def get(self, request, *args, **kwargs):
        category_str = request.GET.get('category')
        if category_str:
            category_id = int(category_str)
        else:
            category_id = 0
        if category_id > 0:
            products_list = Products.objects.filter(category=category_id)
            msg = f"Это фильтр категория {category_id}"

        else:
            products_list = Products.objects.all()
            msg = f"Это просто страница {category_id}"
        categories = Category.objects.all()
        return render(request, template_name=self.template_name,
                      context={'products_list': products_list, 'msg': msg, 'categories': categories})

