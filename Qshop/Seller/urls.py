from django.contrib import admin
from django.urls import path,re_path,include
from Seller.views import *
# from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),

    path('personal_info/', personal_info),
    path('goods_add/', goods_add),



    # path('vue_test/',vue_test),

    path('index/',index),
    re_path('goods_list/(?P<page>\d+)/(?P<status>[01])/',goods_list),
    re_path('goods_status/(?P<state>\w+)/(?P<id>\d+)',good_status),
    ]