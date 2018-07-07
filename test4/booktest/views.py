#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import *
# Create your views here.

def index(request):
    #hero = HeroInfo.objects.get(pk=1)
    #context = {'hero':hero}
    list = HeroInfo.objects.filter(isDelete=False)
    context = {'list': list}
    return render(request,'index.html', context)

def show(request, id, id2):
    context = {'id':id}
    return render(request, 'show.html',context)

# 用于练习模板的继承
def index2(request):
    return render(request, 'index2.html')

def user1(request):
    return render(request, 'user1.html')

def user2(request):
    return render(request, 'user2.html')

# html 转义练习
def html_test(request):
    context ={'t1': '<h1>123</h1>'}
    return render(request, 'html_test.html',context)

# csrf
def csrf1(request):
    return render(request, 'csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

# 验证码
def verify_code(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgcolor = (random.randrange(50,100),random.randrange(50,100),0)
    #规定宽高
    width=100
    height =25
    image = Image.new('RGB',(width,height),bgcolor)
    # 构建字体对象
    font = ImageFont.truetype('FreeMono.ttf', 24)
    #创建画笔
    draw = ImageDraw.Draw(image)
    #创建文本内容
    text = '0123ABCD'
    # 逐个绘制字符mZ
    textTemp =''
    for i in range(4):
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp += textTemp1
        draw.text((i*25,0),
                textTemp1, 
                 (255,255,255),
                 font)
    request.session['code']=textTemp
    # 保存到内存流中
    import cStringIO
    buf = cStringIO.StringIO()
    image.save(buf,'png')
    # 将内容流中的内容输出到客户端
    return HttpResponse(buf.getvalue(), 'image/png')

def verify_test1(request):
    return render(request, 'verifytest.html')

def verify_test2(request):
    input_code = request.POST["code1"]
    site_code =  request.session['code']
    if input_code.lower() == site_code.lower():
        return HttpResponse("ok")
    else:
        return HttpResponse("验证码错误")
