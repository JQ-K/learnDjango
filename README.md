# learnDjango

1.mvc 框架的核心思想是解耦 Django 结构是mvt

. M 表示model，负责与数据库交互

. V 表示view， 是核心，负责接收请求、获取数据、返回结果 -T template,负责呈现内容到浏览器


#### 视图 
. 获取表单单个数据方法，request.POST[' 关键字'] or request.POST.get('关键字')

. 获取表单多个数据 列表, request.POST.getlist('关键字')

> session

    request.session[key]  or  request.session.get(key):