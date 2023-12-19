from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from news.models import News
from .forms import NewsForm

class NewsView(ListView):
    model = News
    fields = '__all__'
    template_name = 'news.html'
    context_object_name = 'newsv'
    # paginate_by = 4



    def get_queryset(self):
        return News.objects.all()


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_queryset(self):
        return News.objects.all()