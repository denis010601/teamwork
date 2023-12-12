from . import views
from django.urls import path

urlpatterns = [
    path('import_export/', views.BrandListView.as_view(), name='brands'),
]