"""
URL configuration for sgtrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from news.views import NewsView, NewsDetailView, NewsListView
from products.views import ProductCreateView, ProductListView, ProductDetailView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', NewsView.as_view(), name='news'),
    path('news_list/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)