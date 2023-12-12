from django.shortcuts import render
from django.views.generic import ListView
from .models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'import_export/brands.html'
