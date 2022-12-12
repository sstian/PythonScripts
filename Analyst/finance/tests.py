from datetime import date

from django.test import TestCase
import pytest


import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Analyst.settings")
django.setup()


from finance.models import Category, Trade
from django.forms.models import model_to_dict


class Test:

    def test_queryset_to_dict_dict(self):
        print()
        print("test hhh")

        categories = Category.objects.all()
        category_detail_dict = {}
        for category in categories:
            category_dict = model_to_dict(category)

            category_trades = category.trade_set.all()
            detail_dict = {}
            for trade in category_trades:

                if trade.detail not in detail_dict.keys():
                    detail_dict.setdefault(trade.detail, model_to_dict(trade))
                else:
                    value = detail_dict.get(trade.detail)
                    value["price"] += trade.price
                    print("value = " + str(value))

            category_dict.setdefault("sub", detail_dict)
            category_detail_dict.setdefault(category.name, category_dict)

        print("category_detail_dict = " + str(category_detail_dict))

    def test_add_trade_tmp(self):
        category_name = "Home/Rent"
        category = Category.objects.get(name=category_name)

        trade = Trade()
        trade.type = True
        trade.datail = "Rent"
        trade.price = 2000
        trade.trade_date = date(2020, 9, 16)
        trade.category = category
        trade.save()

    def test_dele_category(self0):
        catogory = Category.objects.get(name='City')
        # name = request.GET.get('name')  #name，或者看传过来什么
        # 2.删除数据库中对应的记录
        rest = Trade.objects.filter(category=catogory)  # 删除交易表中数据???--还是直接用id就可以？
        rest.delete()
        rest = Category.objects.filter(name='City')  # 删除大目录表中数据
        rest.delete()
        print("ok")

    def test_add_trade(self):
        print()
        category_name = "City"
        category = Category.objects.get(name=category_name)

        trade = Trade()
        trade.type = False
        trade.detail = "citi3"
        trade.price = 2000
        trade.trade_date = date(2020, 10, 1)
        trade.category = category
        trade.save()

        if trade.type is False:
            price_expense = category.expense
            category.update(expense=(price_expense + trade.price))
            print(price_expense, type(price_expense))
        else:
            price_income = category.income
            category.update(income=(price_income + trade.price))

        print("test_add_trade is ok")

    def test_delete_trade(self):
        trade = Trade.objects.get(id=33)
        obj_category = trade.category

        if (trade.type == 0):
            priceExpense = Category.objects.get(id=obj_category.id).expense
            print(priceExpense, type(priceExpense))
            Category.objects.filter(id=obj_category.id).update(expense=float(priceExpense) - trade.price)
        else:
            priceIncome = Category.objects.get(id=obj_category.id).income
            Category.objects.filter(id=obj_category.id).update(income=priceIncome - trade.price)

        rest = Trade.objects.filter(id=trade.id)  # filter() 根据条件进行过滤。
        rest.delete()
        print("test_dele_trade is ok")

