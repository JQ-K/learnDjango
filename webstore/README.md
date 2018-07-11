### 用户注册功能
1. 设计数据库模型 user_info包含字段，名字、密码、邮箱
2. 完成数据库迁移
3. 编辑表单和视图函数
>  表单 method为post，第一个视图函数关联注册主页面
第二个视图函数，关联表单提交按钮，注册内容存入数据库
> 密码存入钱使用sha1加密，并且判断两次密是否一致
最后重定向到登录界面
> 注册时候需要判断用户名是否被注册过，通过Js配合获取到要注册的用户名，然后到数据库中查找有此用户名对象个数，
> js中做出判断如果count=1 提示无法注册， 如果count=0 继续注册

### 用户登录功能
* 设计思路
>  登录页面显示 用户名 密码 输入框和 提交按钮
>  设计登录辅助视图函数， login_handle 处理提交的数据
*  一是要确定数据的用户名和密码是否正确：

>  通过request.POST获取用户名，使用UerInfo.objects.filter(uname=name)获取一个对象列表，通过对象列表长度是否为1确定用户名是否正确

> 用户名正确之后下一步确定密码是否正确，同样request.POS获取密码，注意的是需要比对加密后的密码(sha1)

> 用户名和密码都没问题后，存入Cookie (HttpResposne().set_cookie('uname':uname)),设置cookie的目的是下次打开登录页面自动填充用户名

> 设置session  request.session [] = .. 保存用户名和id，目的是之后其他视图查询方便


* 都没问题之后render到info页面


* model 获取数据使用filter 和get的不同

>  UserInfo.objects.get(id=1)获取的是一个对象可以直接使用属性取值 UserInfo.objects.get(id=1).uname

> UserInfo.objects.filter(id=1) 获得的是一个对象列表，需要现获取里面的元素再取值
  UserInfo.objects.filter(id=1)[0].uname


