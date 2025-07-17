from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, AreaInfo, PicInfo

# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    """ 图书模型管理类 """
    list_display = ["id", "btitle", "bpub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    """ 英雄模型管理类 """
    list_display = ["id", "hname", "hcomment"]

# 关联对象1
class AreaStackedInline(admin.StackedInline):
    # 关联子对象，多的类名
    model = AreaInfo
    # 额外编辑的对象个数
    extra = 2

# 关联对象2
class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):
    """ 地区模型管理类 """
    ## 列表页选项
    # 页面显示字段，可指定方法名，如：parent
    list_display = ["id", "atitle", "parent"]
    # 指定每页显示数据条数
    list_per_page = 10
    # 列表页右侧过滤栏
    list_filter = ["atitle"]
    # 动作下拉列表位置
    actions_on_top = False
    actions_on_bottom = True
    # 列表页上方的搜索框
    search_fields = ["atitle"]

    ## 编辑页选项
    # fields = ["aparent", "atitle"]
    fieldsets = (
        ("基本", {"fields": ["atitle"]}),
        ("高级", {"fields": ["aparent"]})
    )

    inlines = [AreaStackedInline]
    # inlines = [AreaTabularInline]

# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)

admin.site.register(PicInfo)
