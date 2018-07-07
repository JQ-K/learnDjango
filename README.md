# learnDjango

1.mvc 框架的核心思想是解耦 Django 结构是mvt

. M 表示model，负责与数据库交互

. V 表示view， 是核心，负责接收请求、获取数据、返回结果 -T template,负责呈现内容到浏览器


#### 视图 
. 获取表单单个数据方法，request.POST[' 关键字'] or request.POST.get('关键字')

. 获取表单多个数据 列表, request.POST.getlist('关键字')

> session

    request.session[key]  or  request.session.get(key):
    状态保持
        http 协议是无状态协议，实现状态保持使用cookie或者session

        session
            request.session.set_expiry() 设置过期时间

            session 存放地址
            session 依赖于cookie，浏览器会存一个sessionid在cookie中，请求的时候会去服务器比对sessionid

            session 默认存在使用的数据库中，可以单独设置存在redis中
                pip install django-redis-sessions
                settings.py 中设置:
                    SESSION_ENGINE = 'redis_sessions.session'
                    SESSION_REDIS_HOST = 'localhost'
                    SESSION_REDIS_PORT = 6379
                    SESSION_REDIS_DB = 0
                    SESSION_REDIS_PASSWORD = ''
                    SESSION_REDIS_PREFIX = 'session'
                还需要开启redis
