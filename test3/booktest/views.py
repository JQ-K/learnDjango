#coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
     
    #icontext = {'list':list}
    return HttpResponse(request.path)

def detail(request, p1,p2,p3):
    return HttpResponse('year:{},month:{},day:{}'.format(p1,p2,p3))

def get_test1(request):
    return render(request,'test1.html')


def get_test2(request):
    a1= request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request, 'test2.html', context)


def get_test3(request):
    a1 = request.GET.getlist('a')
    context = {'a':a1}
    return render(request, 'test3.html',context)

def post_test1(request):
    return render(request,'post_test1.html')

def post_test2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    print(uhobby)
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender,'uhobby':uhobby}
    return render(request,'post_test2.html',context)

#cookie 练习
def cookie_test(request):
    response = HttpResponse()
    cookie = request.COOKIES
    if cookie.has_key('t1'):
         response.write(cookie['t1'])
    #response.set_cookie('t1','
    return response

#重定向
def redirect_test1(request):
    return HttpResponseRedirect('/booktest/redTest2/')

def redirect_test2(request):
    return HttpResponse('重定向的结果')

# http 是无状态协议，无法记录与网站的交互想要保存需要使用cookie或者session
# 通过用户登录练习session
def session1(request):
    #uname = request.session['myname']
    uname = request.session.get('myname', '未登录')#解决session无值情况下报错问题，使用get获取字典内容
    context ={'uname': uname}
    return render(request,'session1.html', context)
def session2(request):
    return render(request, 'session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0)
    return HttpResponseRedirect('/booktest/session1/')

def session3(request):
    #删除session
    del request.session['myname']
    return HttpResponseRedirect('/booktest/session1/')
