from django.db import models


class Category(models.Model):
    """ Category / Budget """
    name = models.CharField(max_length=40)
    income = models.FloatField(default=0.0)
    expense = models.FloatField(default=0.0)
    budget = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    # 元选项，指定数据表名
    class Meta:
        db_table = "category"


class Trade(models.Model):
    """ Trade(Transaction) / Detail"""
    # True 1 - income, False 0 - expense
    type = models.BooleanField(default=False)
    detail = models.CharField(max_length=40)
    price = models.FloatField(default=0.0)
    trade_date = models.DateField()
    remark = models.CharField(max_length=60)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.detail

    class Meta:
        db_table = "trade"
