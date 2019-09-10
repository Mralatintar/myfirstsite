from django.shortcuts import render, HttpResponseRedirect,render_to_response,HttpResponse
from Seller.models import *
import hashlib
from django.core.paginator import Paginator
from django.http import JsonResponse

def setPassword(password):                  #对密码进行加密
    md5=hashlib.md5()                       #实例化md5方法
    md5.update(password.encode())           #对传入的password进行加密
    result=md5.hexdigest()                  #加密后返回结果给result
    return result
def register(request):
    error_message=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        # username = request.POST.get("username")
        # age = request.POST.get("age")
        # gender = request.POST.get("gender")
        # address = request.POST.get("address")
        # phone_number = request.POST.get("phone_number")
        # photo=request.POST.get("photo")
        if email:
            user=LoginUser.objects.filter(email=email).first()
            if not user:
                new_user=LoginUser()
                new_user.email=email
                # new_user.username=username
                new_user.password=setPassword(password)
                # new_user.age=age
                # new_user.gender=gender
                # new_user.address=address
                # new_user.phone_number=phone_number
                # new_user.photo=photo
                new_user.save()
            else:
                error_message="邮箱已经被注册，请登录"
        else:
            error_message="邮箱不可为空"


    return render(request, "seller/register.html", locals())

def loginValid(fun):#装饰器
    def inner(request,*args,**kwargs):
        # cookie_username=request.COOKIES.get("username")
        # session_username=request.session.get("username")
        # if cookie_username and session_username and session_username==cookie_username:
        cookie_email = request.COOKIES.get("email")                         #提取本地缓存的cookie的email
        session_email = request.session.get("email")                        #提取服务器端的email
        if cookie_email and session_email and session_email == cookie_email:#如果都不为空而且都相等
            return fun(request,*args,**kwargs)                              #执行装饰器
        else:
            return HttpResponseRedirect("/login/")                          #否则跳转到login
    return inner

@loginValid
def index(request):
    return render(request,"seller/index.html",locals())


# 登录

def login(request):
    error_message=""                 #异常状态容器
    if request.method=="POST":      #如果请求是post
        email=request.POST.get("email")     #email等于post请求传过来的name=email值
        password=request.POST.get("password")   #password等于post请求传过来的name=password的值
        if email:                             #如果email不为空
            user=LoginUser.objects.filter(email=email).first()  #调取数据库中LoginUser表中email=email的数据列传给user
            if user:                            #如果user存在（说明网页传来的数据和数据库对的上）
                db_password=user.password       #数据库中对应的密码值给变量db_password
                password=setPassword(password)  #把网页上加密的password赋值给新的password
                if db_password==password:       #如果都经过md5 加密的password值相等
                    response=HttpResponseRedirect("/Seller/index/")    #访问主页index
                    response.set_cookie("email",user.email)         #把数据库中的username下载到本地
                    response.set_cookie("user_id",user.id)         #把数据库中的id下载到本地缓存
                    request.session["email"]=user.email       #把用户信息放到服务器端
                    return response                            #返回请求
                else:
                    error_message="密码错误"
            else:
                error_message="用户名不存在"
        else:
            error_message="邮箱不可为空"
    return render(request,"seller/login.html",locals())

# 退出视图
def logout(request):
    response=HttpResponseRedirect("/login/")        #结果为返回到网页的登录界面
    keys=request.COOKIES.keys()                     #获取已登录的本地缓存的cookie值
    for key in keys:                                #遍历本地的cookie值
        response.delete_cookie(key)                 #结果中删除cookie
    del request.session["username"]                 #删除服务器端的用户信息
    return response


@loginValid
def goods_list(request,status,page=1):              #列表视图
    page=int(page)                                  #页码=1
    if status=="1":                                 #如果 物品状态是1 也就是上架中
        goodses=Goods.objects.filter(goods_status=1)   #筛选数据库中goods_status=1的数据
    elif status=="0":                               #如果 物品状态是0 也就是下架中
        goodses=Goods.objects.filter(goods_status=0)    #筛选数据中goods_status=0的数据
    else:
        goodses=Goods.objects.all()                 #否则就列出所有
    all_goods=Paginator(goodses,10)                 #把筛选出的商品分页器分页出结果给all_goods，all_goods=[1,2,3,4....]，可以循环
    goods_list=all_goods.page(page)                 #goods_list为结果中的第page页
    return render(request,"seller/goods_list.html",locals())

def good_status(request,state,id):             #物品的上架和下架状态（获取状态，ip）
    id=int(id)                                  #转int类型
    goods=Goods.objects.get(id=id)              #获取物品id
    if state=="up":                             #如果传入的数据stata为up
        goods.goods_status=1                    #将物品的状态改为1
    elif state=="down":                         #如果传入的数据stata为down
        goods.goods_status=0                    #将物品状态改为0
    goods.save()                                #保存
    url=request.META.get("HTTP_REFERER","/goods_list/1/1")  #url改为？
    return HttpResponseRedirect(url)            #返回到网页

@loginValid
def personal_info(request):                  #个人中心的设置
    user_id=request.COOKIES.get("user_id")  #获取本地缓存中的cookie
    user=LoginUser.objects.get(id=int(user_id))#user获取id对应的全部信息
    if request.method=="POST":                  #如果会话方式为post
        user.username=request.POST.get("username")      #保存各种数据
        user.gender=request.POST.get("gender")
        user.age = request.POST.get("age")
        user.phone_number = request.POST.get("phone_number")
        user.address = request.POST.get("address")
        photo = request.FILES.get("photo")
        if photo:                                   #如果上传的photo有数据，保存photo
           user.photo=photo
        user.save()             #photo没有数据就只保存数据其他数据
    return render(request, "seller/personal_info.html", locals())


@loginValid
def goods_add(request):                     #创建添加商品方法
    good_type_list=GoodsType.objects.all    #获取表GoodsType中所有数据
    if request.method=="POST":              #如果网页接口是post
        data=request.POST                    #data为网页上接收的所有数据
        files=request.FILES                 #files为接收的files文件，项目中是jpg

        goods=Goods()                       #调用商品表格，实例化
        goods.goods_number = data.get("goods_number")       #把网页上的数据分别加入到表中
        goods.goods_name = data.get("goods_name")
        goods.goods_price = data.get("goods_price")
        goods.goods_count = data.get("goods_count")
        goods.goods_location = data.get("goods_location")
        goods.goods_safe_date = data.get("goods_safe_date")
        goods.goods_pro_time = data.get("goods_pro_time")
        goods.goods_status = 1

        goods_type_id=int(data.get("goods_type"))
        goods.goods_type=GoodsType.objects.get(id=goods_type_id)            #

        picture=files.get("picture")                            #获取网页传来的picture
        goods.picture=picture                                    #实例化图片给数据库

        user_id=request.COOKIES.get("user_id")                   #把本地的的cookie的id给user_id
        goods.goods_store=LoginUser.objects.get(id=int(user_id))    #把用户的id给goods表里的store
        goods.save()                                                #保存结果
    return render(request,"seller/goods_add.html",locals())
# Create your views here.
