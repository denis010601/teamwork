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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_books'] = News.objects.filter(news=self.object)
        return context

    def get_queryset(self):
        return News.objects.all()


