from . import views
from django.urls import path

urlpatterns = [
    path('', views.BrandListView.as_view(), name='brands'),
]