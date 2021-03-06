"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from config import settings

admin.site.site_title = "Admin Store"
admin.site.site_header = "Administración General"
admin.site.index_title = "Administración Store"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("catalogue.urls", namespace='catalogue')),  # '/'
    path('customers/', include("customers.urls", namespace='customers')),
    path('security/', include("users.urls", namespace="users")),
    path('order/', include("orders.urls", namespace="orders")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
