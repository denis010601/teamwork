
from django.urls import path

from .views import *
from . import views
urlpatterns = [

    path('', views.ProductListView.as_view(), name='products'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='products_detail'),
    path('<int:pk>', views.add_review, name='add_review'),
    path('<int:pk>', views.add_review, name='add_rating'),

]