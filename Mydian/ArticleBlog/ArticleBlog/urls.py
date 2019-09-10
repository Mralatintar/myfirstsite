"""ArticleBlog URL Configuration

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
from Article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newlist/',myoneday),
    path('mynote/',mynote),
    path('jishu/',jishu),
    re_path(r'^$',index),
    re_path(r'newlist/(?P<types>\w+)/(?P<p>\d{1,6})', newList),
    re_path('new/(?P<id>\d{1,6})', new),
    path('about/',about),
    path('index/',index),
    path('listpic/',listpic),

    path('aatest/',aatest),
    # path('form_exam/',form_exam),

    path('register/',register),
    path('jqExample/',jqExample),


    path('agp/', ajax_get_page),
    path('agd/',ajax_get_data),

    path('app/',ajax_post_page),
    path('apd/',ajax_post_data),

    path('user_valid/',user_valid),

    path('yonghu_valid/',yonghu_valid),

    path('login/',login),
    path('logout/',logout),



]
