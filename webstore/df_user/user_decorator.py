 #coding:utf-8
from django.shortcuts import redirect 
from django.http import HttpResponseRedirect

#登录验证装饰器,如果未登录转到登录页面

def islogin(func):
	def login_fun(request, *args, **kwargs):
		if request.session.has_key('user_id'):
			return func(request, *args, **kwargs)
		else:
			red = HttpResponseRedirect('/user/login/')
			#下面一行的目的是 如果需要登录，先记录现在路径登录完成后直接转过来
			red.set_cookie('url', request.get_full_path())
			return red

	return login_fun
  
"""
 
 比如:
   http://127.0.0.0.1:8000/200/?type=0
   request.path :表示当前路径  /200/
   request.get_full_path():表示完整路径  /200/?type=0
  """