from django.db import models

# Create your models here.


# class BookInfoManager(models.Manager):
#     """ 自定义图书模型管理器类 """
#     # 应用场景1. 改变查询的结果集
#     def all(self):
#         """ 调用父类all获取数据，过滤，返回"""
#         books = super().all()
#         books = books.filter(is_delete=False)
#         return books
#
#     # 应用场景2. 封装函数：操作模型类对应的数据表（增删改查）
#     def create_book(self, btittle, bpub_date):
#         """ 创建图书类对象，保存进数据库，返回 """
#         # book = BookInfo()
#         book = self.model()
#         book.btitle = btittle
#         book.bpub_date = bpub_date
#         book.save()
#         return book


class BookInfo(models.Model):
    """ 图书模型类 """
    # 标题
    btitle = models.CharField(max_length=20)
    # 出版日期
    bpub_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 软删除标记
    is_delete = models.BooleanField(default=False)

    # 自定义Manager类对象
    # objects2 = BookInfoManager()

    # 后台管理显示
    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """ 英雄模型类 """
    # 名字
    hname = models.CharField(max_length=20)
    # 性别：True - 男性，False - 女性
    hsex = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=128)
    # 关系属性，外键，BookInfo:HeroInfo=一对多
    # 关系属性对应表的字段名格式：关系属性名_id
    hbook = models.ForeignKey("BookInfo", on_delete=models.CASCADE)
    # 软删除标记
    is_delete = models.BooleanField(default=False)

    # 后台管理显示
    def __str__(self):
        return self.hname


class AreaInfo(models.Model):
    """ 地区模型类"""
    # 地区名称
    atitle = models.CharField(verbose_name="标题", max_length=20)
    # 关系属性，父级地区
    aparent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    # 后台管理显示
    def __str__(self):
        return self.atitle

    def parent(self):
        if self.aparent is None:
            return ""
        return self.aparent.atitle
    # 指定排序字段
    parent.admin_order_field = "atitle"
    # 显示字段描述
    parent.short_description = "父级地区"

    # 元选项，指定数据表名
    class Meta:
        db_table = "areainfo"


class PicInfo(models.Model):
    """ 图片模型类 """
    goods_pic = models.ImageField(upload_to="booktest")

    class Meta:
        db_table = "picinfo"
