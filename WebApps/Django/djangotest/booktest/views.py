from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from booktest.models import BookInfo, AreaInfo, PicInfo
from datetime import date, datetime, timedelta

# Create your views here.
# 定义视图函数，HttpRequest
# http://127.0.0.1:8000/index


def login_required(view_func):
    """ 登录判断装饰器 """
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if "is_login" in request.session:
            return view_func(request, *view_args, **view_kwargs)
        else:
            return redirect("/login")
    return wrapper


def home(request):
    return redirect("/select_area")


def index(request):
    # 进行处理，和M,T交互
    # return HttpResponse("老铁，666")

    # temp = loader.get_template("booktest/index.html")
    # context = {"content": "hello word", "list": list(range(1,10))}
    # return HttpResponse(temp.render(context))

    print("views.py - index()")
    return render(request, "booktest/index.html",  {"content": "hello word", "list": list(range(1, 10))})


def show_books(request):
    """ 显示图书信息 """
    books = BookInfo.objects.all()
    return render(request, "booktest/show_books.html", {"books": books})


def detail(request, bid):
    """ 显示英雄信息"""
    book = BookInfo.objects.get(id=bid)
    heroes = book.heroinfo_set.all()
    return render(request, "booktest/detail.html", {"book": book, "heroes": heroes})


def index2(request):
    """ 显示图书信息 """
    # 查询所有图书信息
    books = BookInfo.objects.all()
    # 使用模板
    return render(request, "booktest/index2.html", {"books": books})


def create(request):
    """ 新增一本图书 """
    # 创建对象
    book = BookInfo()
    book.btitle = "流星蝴蝶剑"
    book.bpub_date = date(1990, 1, 1)
    # 保存进数据库
    book.save()
    # 返回应答，浏览器页面跳转，重定向
    # return HttpResponse("ok")
    # return HttpResponseRedirect("/index2")
    return redirect("/index2")


def delete(request, bid):
    """ 删除点击的图书 """
    # 获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 删除
    book.delete()
    # 重定向
    return redirect("/index2")


def areas(request):
    """ 获取城市信息 """
    area = AreaInfo.objects.get(atitle="北京市区")
    # 查询上级区域
    parent = area.aparent
    # 查询下级区域
    children = area.areainfo_set.all()
    return render(request,
                  "booktest/areas.html",
                  {"area": area, "parent": parent, "children": children})


def showarg(request, num):
    return HttpResponse(num)


# @csrf_exempt
def login(request):
    """ 显示登陆界面 """
    # 用户是否登录，是则直接跳转
    if "is_login" in request.session:
        return redirect("/change_pwd")
    # 获取cookie
    username, password = "", ""
    if "username" in request.COOKIES:
        username = request.COOKIES["username"]
    if "password" in request.COOKIES:
        password = request.COOKIES["password"]
    return render(request, "booktest/login.html",
                  {"username": username, "password": password})


# @csrf_exempt
def login_check(request):
    """ 登陆校验视图"""
    # request.POST 保存的是post方式提交的数据 QueryDict
    # request.GET 保存的是get方式提交的数据
    # 获取用户名密码，登陆校验（查找数据库）
    username = request.POST.get("username")
    password = request.POST.get("password")
    remember = request.POST.get("remember")
    # 验证码比对：用户输入的 VS Session中的
    vcode = request.POST.get("vcode")
    verify_code = request.session.get("verifycode")
    if vcode != verify_code:
        return redirect("/login")

    if username == "aaa" and password == "123":
        # 记住用户名和密码， 复选框：勾选=on, 未勾选=None
        response = redirect("/change_pwd")
        if remember == "on":
            # 设置cookie，过期时间7天，max_age单位为秒
            response.set_cookie("username", username, max_age=7*24*3600)
            response.set_cookie("password", password, expires=datetime.now()+timedelta(days=7))
            # 记住用户登录状态，只要Session存在is_login，认为已登录
            request.session["is_login"] = True
            # 记录登录的用户名
            request.session["username"] = username
        return response
    else:
        return redirect("/login")


@login_required
def change_pwd(request):
    """ 显示修改密码页面 """
    return render(request, "booktest/change_pwd.html")


@login_required
def change_pwd_action(request):
    """ 模拟修改密码处理 """
    # 获取新密码和用户名，修改数据库，返回应答
    pwd = request.POST.get("pwd")
    username = request.session.get("username")
    return HttpResponse("%s 修改密码为: %s" % (username, pwd))


# 折线图对应的的模板
def showlinediagram(request):
    return render(request, 'booktest/showlinediagram.html')


def ajax_test(request):
    """" 显示AJAX页面 """
    return render(request, "booktest/ajax_test.html")


def ajax_handle(request):
    """ AJAX请求处理，返回JSON数据"""
    return JsonResponse({"res": 1})


@csrf_exempt
def login_ajax(request):
    """ 显示AJAX登陆页面 """
    return render(request, "booktest/login_ajax.html")


@csrf_exempt
def login_ajax_check(request):
    """ AJAX登陆校验 """
    # 获取用户名密码，校验返回JSON数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "aaa" and password == "123":
        return JsonResponse({"res": 1})
    else:
        return JsonResponse({"res": 0})


def temp_filter(request):
    """ 模板过滤 """
    books = BookInfo.objects.all()
    context = {"books": books}
    return render(request, "booktest/temp_filter.html", context)


def temp_inherit(request):
    """ 模板继承 """
    return render(request, "booktest/child.html")


def html_escape(request):
    """ HTML转义 """
    return render(request, "booktest/html_escape.html",
                  {"content": "<h1>hello</h1>"})

# 验证码
from PIL import Image, ImageDraw, ImageFont
from six import BytesIO
def verify_code(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高、GRB
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 30
    # 创建画面对象
    im = Image.new("RGB", (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rand_str = ""
    for s in range(0, 4):
        rand_str += str[random.randrange(0, len(str))]
    # 构造字体对象、颜色
    font = ImageFont.truetype("ebrima.ttf", 23)
    font_color = (2555, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制文本
    draw.text((5, 0), rand_str[0], font=font, fill=font_color)
    draw.text((25, 0), rand_str[1], font=font, fill=font_color)
    draw.text((50, 0), rand_str[2], font=font, fill=font_color)
    draw.text((75, 0), rand_str[3], font=font, fill=font_color)

    # 释放画笔
    del draw
    # 引入Session，用于进一步验证
    request.session["verifycode"] = rand_str
    # 内存文件操作，保存图像在内存中
    buf = BytesIO()
    im.save(buf, "png")
    # 返回给客户端，MIME类型
    return HttpResponse(buf.getvalue(), "image/png")


def url_reverse(request):
    """ url反向解析 """
    return render(request, "booktest/url_reverse.html")


def show_args(request, a, b):
    """ url反向解析：位置参数 """
    return HttpResponse(a + ":" + b)


def show_kwargs(request, c, d):
    """ url反向解析：关键字参数 """
    return HttpResponse("c=" + c + ":" + "d=" + d)


def view_reverse(request):
    """ 视图函数反向解析"""
    url = reverse("booktest:index")
    url2 = reverse("booktest:show_args", args=(10, 20))
    url3 = reverse("booktest:show_kwargs", kwargs={"c":30, "d":40})
    return redirect(url3)


def static_file(request):
    print(settings.STATICFILES_DIRS)
    return render(request, "booktest/static_file.html")


# /upload_pic
def upload_pic(request):
    """ 显示上传图片页面 """
    return render(request, "booktest/upload_pic.html")


def upload_handle(request):
    """ 显示上传图片页面 """
    # 1. 获取上传文件的处理对象
    pic = request.FILES["pic"]
    # 2. 创建文件
    save_path = f"{settings.MEDIA_ROOT}/booktest/{pic.name}"
    with open(save_path, "wb") as file:
        # 3. 获取上传文件内容并写入到创建的文件中
        for content in pic.chunks():
            file.write(content)
    # 4. 保存记录到数据库
    PicInfo.objects.create(goods_pic=f"booktest/{pic.name}")
    # 5. 返回
    return HttpResponse("ok")


from django.core.paginator import Paginator
def page_area(request, pindex):
    """ 分页 """
    # 1. 查询信息
    areas = AreaInfo.objects.filter(aparent__isnull=False)
    # 2. 分页，每页显示条数
    paginator = Paginator(areas, 5)
    # 3. 获取第pindex页的内容，默认第1页
    if pindex == "":
        pindex = 1
    else:
        pindex = int(pindex)
    # page是Page类的实例对象
    page = paginator.page(pindex)
    # 4. 渲染模板
    return render(request, "booktest/page_area.html", {"page": page})


def select_area(request):
    return render(request, "booktest/select_area.html")


def prov(request):
    """ 下拉选择：获取所有省 """
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    # 拼接为JSON数据
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))

    return JsonResponse({"data": area_list})


def city(request, pid):
    """ 获取pid下级地区信息 """
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aparent__id=pid)
    # 拼接为JSON数据
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))

    return JsonResponse({"data": area_list})

