# from django.http import HttpResponse
# from django.template.loader import get_template
# from django.shortcuts import render_to_response
# from Article.models import *
#
# def index(request):
#     template=get_template("index.html")
#     result=template.render({})
#     return HttpResponse(result)
#
#
#
# def newList(request):
#     # article_list=Article.objects.all()
#     # print(article_list)
#     # article_list=Article.objects.filter(title='匆匆')
#     article_list=Article.objects.order_by("id")
#     # print(article_list)
#     return render_to_response("newlist.html",locals())
#
#
# def new(request):
#     return render_to_response("new.html")
#
#
#
# def about(request):
#     return render_to_response("about.html")
#
# def listpic(request):
#     return render_to_response("listpic.html")
#




