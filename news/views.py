from django.views.generic import DetailView, ListView, TemplateView

from news.models import News
from .forms import NewsForm

class NewsView(TemplateView):
    model = News
    fields = '__all__'
    template_name = 'news.html'

    def get_queryset(self):
        return News.objects.all()

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_queryset(self):
        return News.objects.all()
