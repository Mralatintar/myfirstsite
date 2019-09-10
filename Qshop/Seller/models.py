from django.db import models
class LoginUser(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=32)

    username=models.CharField(max_length=32,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    photo=models.ImageField(upload_to='seller/images',null=True,blank=True)  #default="seller/image/334.jpg"
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=32,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    user_type=models.IntegerField(default=0)    #买家0 卖家1 管理员是2

class GoodsType(models.Model):
    type_label=models.CharField(max_length=32)
    type_description=models.TextField()
    picture=models.ImageField(upload_to="seller/images")
class Goods(models.Model):
    goods_number=models.CharField(max_length=11)
    goods_name=models.CharField(max_length=32)
    goods_location=models.CharField(max_length=254)
    goods_price=models.FloatField()
    goods_pro_time=models.DateField()
    goods_safe_date=models.IntegerField()
    goods_count = models.IntegerField()
    goods_status=models.IntegerField(default="1")#0为下架，1 为在售

    picture=models.ImageField(upload_to="seller/images")
    goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
    goods_store=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,default=1)
# Create your models here.
