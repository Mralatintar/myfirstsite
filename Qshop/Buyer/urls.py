from django.contrib import admin
from django.urls import path,re_path,include
from Buyer.views import *

urlpatterns = [
    path('login/',login),
    path('index/',index),
    path('register/',register),
    path('logout/', logout),

    path('goods_list/', goods_list),
    path('user_center_info/', user_center_info),

    re_path('goods_detail/(?P<id>\d+)/', goods_detail),
    ]