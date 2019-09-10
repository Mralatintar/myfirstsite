from django.db import models
class Author(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    gender=models.CharField(max_length=32)
    birthday=models.DateField()
    email=models.EmailField()
    adress=models.TextField()
    photo=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class ArticleType(models.Model):
    label=models.CharField(max_length=32)
    description=models.TextField()
    def __str__(self):
        return self.label

class Article(models.Model):
    """
       文章和作者 多对一
       文章和类型 多对多
       """
    title=models.CharField(max_length=32)
    article_author=models.ForeignKey(to=Author,on_delete=models.CASCADE)
    description=models.TextField()
    content=models.TextField()
    article_type=models.ManyToManyField(to=ArticleType)
    public_time=models.DateField(auto_now=True)
    picture=models.ImageField(upload_to='images')

    reconment=models.IntegerField(default=0)
    click=models.IntegerField(default=0)
    def __str__(self):
        return self.title


class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    email=models.EmailField()

# import pymysql
#
# connect=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="111111",
#     datebase="articleblog"
# )
# cursor=connect.cursor()
# sql="select name from article_article limit 100"
#
# result=cursor.execute(sql)
#
# for data in cursor.fetchall():
#     connect.commit()



# Create your models here.
