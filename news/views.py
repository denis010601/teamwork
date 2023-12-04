from django.shortcuts import render
from django.views.generic import CreateView

from news.models import News


class NewsView(CreateView):
    model = News
    fields = '__all__'
    template_name = 'news.html'

    def get_queryset(self):
        return News.objects.all()