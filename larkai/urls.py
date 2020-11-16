"""larkai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.doc_reg,name='doc_reg'),
    path('doc_log',views.doc_log,name='doc_log'),
    path('home',views.home,name='home'),
    path('reading',views.reading,name='reading'),
    path('fetch_value', views.fetch_value, name='fetch_value'),
    path('fetch_value2', views.fetch_value2, name='fetch_value2'),
    path('fetch_ecg', views.fetch_ecg, name='ecg'),
    path('final',views.final,name='final')
]
