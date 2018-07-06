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
    #response.set_cookie('t1','abc')
    return response

#重定向
def redirect_test1(request):
    return HttpResponseRedirect('/booktest/redTest2/')

def redirect_test2(request):
    return HttpResponse('重定向的结果')
