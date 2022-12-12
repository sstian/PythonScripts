
import json
from datetime import datetime, date

from django.forms.models import model_to_dict
from django.shortcuts import render

from finance.models import Category, Trade


class CJsonEncoder(json.JSONEncoder):
    """ Serialize Date type object """

    def default(self, obj):

        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class Utils:

    @staticmethod
    def queryset_to_dict_list(queryset, is_print=False):
        """

        :param queryset: [{"key1": "value1"}, ["key2": value2}, ...]
        :param is_print:
        :return:
        """
        cat_list = []
        for cat in queryset:
            cat_dict = model_to_dict(cat)
            cat_list.append(cat_dict)

        if is_print:
            print("queryset_to_dict_list = " + str(cat_list))
        return cat_list

    @staticmethod
    def queryset_to_set_dict(queryset, is_print=False):
        """

        :param queryset: {"key1": {v1}, "key2": {v2, v3}, ...}
        :param is_print:
        :return:
        """
        category_detail_dict = {}
        for category in queryset:
            category_trades = category.trade_set.all()

            detail_set = set()
            for trade in category_trades:
                detail_set.add(trade.detail)
            detail_list = list(detail_set)

            category_detail_dict.setdefault(category.name, detail_list)

        if is_print:
            print("category_detail_dict = " + str(category_detail_dict))
        return category_detail_dict

    @staticmethod
    def response_data_bill(queryset, is_print=False):
        expenses, income, budget, accounts = 0.0, 0.0, 0.0, 0.0
        for category in queryset:
            expenses += category.expense
            income += category.income
            budget += category.budget
            accounts = income - expenses + 20000
        percent = expenses / budget * 100
        remain = budget - expenses
        percent_ei = expenses / income * 100
        save = income - expenses
        bill = {"expenses": round(expenses, 2), "income": round(income, 2),
                "budget": round(budget, 2), "accounts": round(accounts, 2),
                "percent": round(percent, 2), "remain": round(remain, 2),
                "percent_ei": round(percent_ei, 2), "save": round(save, 2)}

        if is_print:
            print("bill = " + str(bill))
        return bill

    @staticmethod
    def queryset_to_dict_dict(queryset, is_print=False):
        """

        :param queryset:
        :param is_print:
        :return:
        """
        category_detail_dict_dict = {}
        for category in queryset:
            category_dict = model_to_dict(category)

            category_trades = category.trade_set.all()
            detail_dict = {}
            for trade in category_trades:
                if trade.detail not in detail_dict.keys():
                    detail_dict.setdefault(trade.detail, model_to_dict(trade))
                else:
                    value = detail_dict.get(trade.detail)
                    value["price"] += float(trade.price)
                    value["remark"] = trade.remark

            category_dict.setdefault("sub", detail_dict)
            category_detail_dict_dict.setdefault(category.name, category_dict)

        if is_print:
            print("category_detail_dict_dict = " + str(category_detail_dict_dict))
        return category_detail_dict_dict


    @staticmethod
    def render_index_page(request, template_name):
        categories = Category.objects.all()
        trades = Trade.objects.all()

        # 1. contents: category - details
        # category_detail_dict = {'Home/Rent': {'Rent', 'House Loan'}, 'Utilities': {'CellPhone', 'Electricity', 'Water', 'Internet'}, 'Food': {'Dinner', 'Breakfast', 'Fruit', 'Snacks', 'Lunch'}, 'Groceries': {'Necessary', 'Clothes'}, 'Fund money': {''}, 'Entertainment': {'Sport', 'KTV'}, 'Insurance/Medical': {'Insurance', 'Medical'}, 'Travel': {'Taxi', 'Bus', 'Subway'}, 'Salary': {''}}
        category_detail_dict = Utils.queryset_to_set_dict(categories, True)

        # 2. categories: json serialization; set cannot be serialized -> list
        # queryset_to_dict_list = [{'id': 1, 'name': 'Home/Rent', 'income': 0.0, 'expense': 8500.0, 'budget': 2000.0}, {'id': 2, 'name': 'Utilities', 'income': 0.0, 'expense': 212.0, 'budget': 2500.0}, {'id': 3, 'name': 'Food', 'income': 0.0, 'expense': 135.0, 'budget': 3000.0}, {'id': 4, 'name': 'Groceries', 'income': 0.0, 'expense': 626.0, 'budget': 3500.0}, {'id': 5, 'name': 'Fund money', 'income': 1000.0, 'expense': 0.0, 'budget': 0.0}, {'id': 6, 'name': 'Entertainment', 'income': 0.0, 'expense': 280.0, 'budget': 1000.0}, {'id': 7, 'name': 'Insurance/Medical', 'income': 0.0, 'expense': 901.0, 'budget': 900.0}, {'id': 8, 'name': 'Travel', 'income': 0.0, 'expense': 23.0, 'budget': 1500.0}, {'id': 9, 'name': 'Salary', 'income': 3000.0, 'expense': 0.0, 'budget': 0.0}]
        cat_list = Utils.queryset_to_dict_list(categories, True)

        # 3. bill / bills: expense, income, budget, accounts
        # bill = {'expenses': 10677.0, 'income': 4000.0, 'budget': 14400.0, 'accounts': -10400.0, 'percent': 74.15, 'remain': 3723.0}
        bill = Utils.response_data_bill(categories, True)

        # 4. details:
        category_detail_dict_dict = Utils.queryset_to_dict_dict(categories, True)

        return render(request, template_name,
                      {"bill": bill,
                       "contents": json.dumps(category_detail_dict),
                       "categories": json.dumps(cat_list),
                       "bills": json.dumps(bill),
                       "details": json.dumps(category_detail_dict_dict, cls=CJsonEncoder)})

