from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from products import models
from products.models import Products

class HomeView(TemplateView):
    template_name = 'products/home.html'


