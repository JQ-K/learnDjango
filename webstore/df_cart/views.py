# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect

from models import *
from df_user import user_decorator
# Create your views here.
@user_decorator.islogin
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {'title': '购物车',
               'page_name':1,
               'carts':carts }
    return render(request,'df_cart/cart.html')


def add(request, gid, count):
    #用户uid购买了gid商品,数量为count
    #gid和count即商品id和数量可以通过url正则获取到

    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    #查询购物车中是否已经有了此商品,如果有则加1,没有新增
    #通过 user_id 和goods_id定位购物车
    #filter得到的对象是个列表
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >=1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    #保存到数据库
    cart.save()

    #如果是ajax请求则返回json,否则转向购物车
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return  redirect('/cart/')


@user_decorator.islogin
def edit(request,cart_id,count): 
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

@user_decorator.islogin
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)
