from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, DetailView

from news.models import News
from .forms import NewsForm

class NewsView(CreateView):
    model = News
    fields = '__all__'
    template_name = 'news.html'

    def get_queryset(self):
        return News.objects.all()

class NewsDetailView(DetailView):
    model = News
    form_class = NewsForm
    fields = '__all__'
    template_name = 'news_detail.html'

    def get_queryset(self):
        return News.objects.all()


