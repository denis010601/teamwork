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

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include



urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('news/', NewsView.as_view(), name='news'),
    path('brands/', include('import_export.urls')),
=======
    path('admin/', admin.site.urls, name='admin'),
<<<<<<< HEAD
    path('', include('products.urls')),
>>>>>>> c1219f96c33c92fc429c6d63e987d700056e8ecc
=======
    path('', include('home.urls')),
>>>>>>> 6814f243ba46c80902054d781a23c38394fe4af6
    path('products/', include('products.urls')),
    path('news/', include('news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)