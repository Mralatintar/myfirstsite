from django.http import HttpResponse
from django.template.loader import get_template

# def page_list(request,page,day,age):
#     template=get_template("index.html")
#     result=template.render({"page":page,"ti":day,"titi":age})
#     return HttpResponse(result)
def jieshao(requst,name,age,jia):
    template=get_template("xiaowang.html")
    result=template.render({"mz":name,"nl":age,"jiating":jia})
    return HttpResponse(result)

def teachertb(request):
    data={
        "teacher":[
            {"name":"冯浩","age":18},
            {"name":"杨钊","age":19},
            {"name":"胡清杰","age":9999},
            {"name":"龙哥","age":20},
        ],
        "commit":"<script>alert('你好啊,小白')</script>"
    }
    temp=get_template("teacherhtml.html")
    result=temp.render(data)
    return HttpResponse(result)

fulucky="""《Better Now》是由美国说唱歌手波兹·马龙录唱的一首流行歌曲，词曲由波兹·马龙、路易斯·贝尔、弗兰克·杜克斯、比利·沃尔什合作编写，该歌曲被收录在波兹·马龙的第二张录音室专辑《Beerbongs & Bentleys》 [1]  。
You probably think that you are better now, better now
You only say that 'cause I'm not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
You know I say that I am better now, better now
I only say that 'cause you're not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
I did not believe that it would end, no
Everything came second to the Benz oh
You're not even speaking to my friends, no
You knew all my uncles and my aunts though
Twenty candles, blow 'em out and open your eyes
We were looking forward to the rest of our lives
Used to keep my picture posted by your bedside
Now it's in your dresser with the socks you don't like
And I'm rollin', rollin', rollin', rollin'
With my brothers like it's Jonas, Jonas
Drinkin' Henny and I'm tryna forget
But I can't get this shit outta my head
You probably think that you are better now, better now
You only say that 'cause I'm not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
You know I say that I am better now, better now
I only say that 'cause you're not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
I seen you with your other dude
He seemed like he was pretty cool
I was so broken over you
Life it goes on, what can you do?
I just wonder what it’s gonna take
Another foreign or a bigger chain
Because no matter how my life has changed
I keep on looking back on better days
You probably think that you are better now, better now
You only say that 'cause I'm not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
You know I say that I am better now, better now
I only say that 'cause you're not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
Oh-oh
I promise
I swear to you I'll be okay
You're only the love of my life (love of my life)
You probably think that you are better now, better now
You only say that 'cause I'm not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
You know I say that I am better now, better now
I only say that 'cause you're not around, not around
You know I never meant to let you down, let you down
Woulda gave you anything, woulda gave you everything
Oh-oh
"""
print(fulucky)
articles=[
    {"id":1,"title":"爱情买卖","author":"老坛酸菜","public_time":"2018-1-6","content":"没有买卖就没有杀害","image":"image/lths.jpg"},
    {"id":2,"title":"地主财神爷","author":"瑞哥","public_time":"2018-6-8","content":"我是MVP","image":"image/amz.jpg"},
    {"id":3,"title":"BetterNow","author":"福乐小妞","public_time":"2017-11-2","content":fulucky,"image":"image/flxg.jpg"},
    {"id":4,"title":"天蓬元帅","author":"暗影猎手","public_time":"2017-2-16","content":"天蓬元帅准备就绪","image":"image/lyj.jpg"},
    {"id":5,"title":"无限猖狂","author":"周冬雨咯","public_time":"2018-1-6","content":"你的虾王，无限猖狂","image":"image/xdx.jpg"},
    {"id":6,"title":"演员启示录","author":"人才","public_time":"2018-1-6","content":"人家真的走了","image":"image/zxzb.jpg"}

]
def page_list(request):
    template=get_template("page_list.html")
    result=template.render({"articles":articles})
    return HttpResponse(result)

def page(request,id):
    id=int(id)
    article=""
    for art in articles:
        if art["id"]==id:
            article=art
            break
    template=get_template("page.html")
    result =template.render({"article":article})
    return HttpResponse(result)