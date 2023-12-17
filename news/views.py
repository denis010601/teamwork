from django.views.generic import DetailView, ListView
from news.models import News


class NewsView(ListView):
    model = News
    fields = '__all__'
    template_name = 'news.html'
    context_object_name = 'newsv'
    # paginate_by = 4



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