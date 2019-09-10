"""Mydian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from Mydian.anniya import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path('xiaoming/(?P<page>\d{1,2})/(?P<day>\d{1,2})/(?P<age>\d{1,2})',page_list),
    # re_path('xiaowang/(?P<name>\d{1,2})/(?P<age>\d{1,2})/(?P<jia>\d{1,2})',jieshao),
    path('tl/',teachertb),
    path('page_list/',page_list),
    re_path('page/(?P<id>\d{1,2})/',page)








]
