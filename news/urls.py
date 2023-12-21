
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', NewsView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]