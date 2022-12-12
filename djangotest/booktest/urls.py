from django.conf.urls import url
from django.urls import path, re_path
from booktest import views

# 配置url，使url地址和视图对应，严格匹配开头和结尾
# http://127.0.0.1:8080/
urlpatterns = [
    # 通过url函数设置url路由配置项
    # url(r'^index$', views.index),
    path('', views.home),
    url('index', views.index, name="index"),    # url反向解析
    re_path(r'^books$', views.show_books),      # 显示图书信息
    re_path(r'^books/(\d+)$', views.detail),    # 显示英雄信息
    re_path(r'^index2', views.index2),         # 图书信息
    re_path(r'^create$', views.create),         # 新增图书
    re_path(r'^delete(\d+)$', views.delete),  # 删除点击的图书
    re_path(r'^areas$', views.areas),           # 自关联 城市
    re_path(r'^showarg(\d+)$', views.showarg), # 捕获位置参数
    # re_path(r'^showarg(?P<num>\d+)$', views.showarg), # 捕获关键字参数
    re_path(r'^login$', views.login), # 显示登陆页面
    re_path(r'^login_check$', views.login_check), # 登陆校验
    re_path(r'^change_pwd$', views.change_pwd),
    re_path(r'^change_pwd_action$', views.change_pwd_action),
    re_path(r'^linediagram/$', views.showlinediagram),
    re_path(r'^ajax_test$', views.ajax_test),
    re_path(r'^ajax_handle$', views.ajax_handle),
    re_path(r'^login_ajax$', views.login_ajax),
    re_path(r'^login_ajax_check$', views.login_ajax_check),
    re_path(r'^temp_filter$', views.temp_filter),
    re_path(r'^temp_inherit$', views.temp_inherit),
    re_path(r'^html_escape$', views.html_escape),
    re_path(r'^verify_code$', views.verify_code),
    re_path(r'^url_reverse$', views.url_reverse),
    url(r'^show_args/(\d+)/(\d+)$', views.show_args, name='show_args'),
    url(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$', views.show_kwargs, name='show_kwargs'),
    re_path(r'^view_reverse$', views.view_reverse),
    re_path(r'^static_file$', views.static_file),
    re_path(r'^upload_pic$', views.upload_pic),
    re_path(r'^upload_handle$', views.upload_handle),
    re_path(r'^page_area(?P<pindex>\d*)$', views.page_area),
    re_path(r'^select_area$', views.select_area),
    re_path(r'^prov$', views.prov),
    re_path(r'^city(\d+)$', views.city),
]