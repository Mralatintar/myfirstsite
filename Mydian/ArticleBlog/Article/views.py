from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from Article.models import *
from functools import partial


# def index(request):
#     template=get_template("index.html")
#     result=template.render({})
#     return HttpResponse(result)

def set_page(page_list,page):
    """
        page_list  # 页码范围
        page #页码
        想要当前页码的前两页和后两页
        """
    if page - 3 < 0:
        start = 0
    else:
        start = page - 3
    if page + 2 > 49:
        end = 49
    else:
        end = page + 2
    return list(page_list[start:end])


def newList(request,types,p):
    # article_list=Article.objects.all()
    # print(article_list)
    # article_list=Article.objects.filter(title='匆匆')

    p = int(p)
    page_size=6
    articles=ArticleType.objects.get(label=types).article_set.order_by("-public_time")
    article_list=Paginator(articles,page_size) #进行分页
    page_article=article_list.page(p)#返回对应页的数据
    page_range=set_page(article_list.page_range,p)#返回对应页的页码
    return render_to_response("newlist.html", locals())
    # article_list=Article.objects.order_by("id")
    # print(article_list)


def myoneday(request):
    # article=Article.objects.get()
    article_list=ArticleType.objects.get(label='个人日记').article_set.order_by("-public_time")[:6]
    return render_to_response("myoneday.html",locals())

def mynote(request):
    article_list = ArticleType.objects.get(label='学习笔记').article_set.order_by("-public_time")
    return render_to_response("mynote.html", locals())
#new/16636   是文章内容

def jishu(request):
    article_list=ArticleType.objects.get(label='技术文章').article_set.order_by("-public_time")
    return render_to_response("jishu.html",locals())


def new(request,id):
    article=Article.objects.get(id=id)
    return render_to_response("new.html",locals())



def about(request):
    return render_to_response("about.html", locals())

def listpic(request):
    return render_to_response("listpic.html")


#装饰器

def loginValid(fun):
    def inner(request,*args,**kwargs):
        username=request.COOKIES.get("username")
        session_username=request.session.get("username")
        if username and session_username:
            return fun(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner

@loginValid #index = loginValid(index)
def index(request):
    """
       1、查询最新的6条
       2、查询推荐7条
       3、查询排行榜点击率前12
       """
    username=request.COOKIES.get("username")
    # if username:
    new_article=Article.objects.order_by("-public_time")[:6]
    recom_article=Article.objects.filter(reconment=1).order_by("-public_time")[:7]
    click_article=Article.objects.order_by("-click")[:12]
    return render_to_response("index.html",locals())
    # else:
    #     return HttpResponseRedirect("/login/")
from django.shortcuts import render

def aatest(request):
    searchkey=request.GET.get("MyKey")
    articles=[]
    if searchkey:
        articles=Article.objects.filter(title__contains=searchkey)
        addx=len(articles)
    return render(request,"aatest.html",locals())

def form_exam(request):

    searchkey=request.GET.get("MyKey")
    articles=[]
    if searchkey:
        articles=Article.objects.filter(title__contains=searchkey)
    return render(request,"form_exam.html",locals())


import hashlib

def setPassword(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

from Article.forms import Register

def register(request):
    register_form=Register()
    if request.method=="POST":
        data_valid=Register(request.POST)
        if data_valid.is_valid():
            clean_data=data_valid.cleaned_data
            username=clean_data.get('username')
            password=clean_data.get('password')
            email=clean_data.get('email')
            u=User()
            u.username=username
            u.password=setPassword(password)
            u.email=email
            u.save()
            succeed="恭喜你，注册成功"
        else:
            errors=data_valid.errors
    return render(request,"register.html",locals())

def jqExample(request):
    return render(request,"jqExample.html",locals())

from django.http import JsonResponse

def ajax_get_page(request):
    return render(request,"ajax_get_page.html",locals())

def ajax_get_data(request):
    return JsonResponse({"ojbk":"来自后台的数据的ojbk","ok":"我是ok"})



def ajax_post_page(request):
    return render(request,"ajax_post_page.html")

def ajax_post_data(request):
    return JsonResponse({"hello":"来自后台的数据的字符串"})

def user_valid(request):
    email=request.GET.get("email")
    result={"code":"400","data":""}
    if email:
        user=User.objects.filter(email=email).first()
        if user:
            result["data"]="当前邮箱已经完成注册"
        else:
            result["code"]="200"
            result["data"]="当前邮箱可以注册"
    else:
        result["data"]="邮箱不可为空"
    return JsonResponse(result)

def yonghu_valid(request):
    username=request.GET.get("username")
    result={"code":"400","data":""}
    if username:
        user=User.objects.filter(username=username).first()
        if user:
            result["data"]="当前用户名已经完成注册"
        else:
            result["code"]="200"
            result["data"]="当前用户名可以注册"
    else:
        result["data"]="用户名不可为空"
    return JsonResponse(result)

from django.http import HttpResponseRedirect

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username).first()
        if user:
            db_password=user.password
            password=setPassword(password)
            if password==db_password:
                response=HttpResponseRedirect("/index/")
                response.set_cookie("username","xiaohaizi")
                response.set_cookie("age","16")
                request.session["username"]=user.username
                return response
    return render(request,"login.html")

def logout(request):
    response=HttpResponseRedirect("/login/")
    response.delete_cookie("username")
    response.delete_cookie("age")
    del request.session["username"]
    return response






# def register(request):
#     register_form = Register()
#     if request.method == "POST": #判断请求方式
#         username = request.POST.get("username")  #获取用户名
#         password = request.POST.get("password")  #获取密码
#         if username and password: #判断用户名和密码
#             u = User() #实例化模型
#             u.username = username #保存用户名
#             u.password = setPassword(password) #保存密码
#             u.save() #保存数据
#     return render(request,"register.html",locals())

# Create your views here.
