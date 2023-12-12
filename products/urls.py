<<<<<<< HEAD
from django.urls import path
from .views import *


urlpatterns = [
    path(),
=======
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
>>>>>>> develop
]