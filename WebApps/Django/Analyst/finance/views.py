import json

from django.core.serializers import serialize
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from finance.models import Category
from finance.models import Trade
from finance.utils import Utils

def home(request):
    return redirect("/index")


def show(request):
    categories = Category.objects.all()
    trades = Trade.objects.all()

    # {"name": {"detail1", "detail2"}, ...}
    category_detail_dict = {}
    for category in categories:
        category_trades = category.trade_set.all()

        detail_set = set()
        for trade in category_trades:
            detail_set.add(trade.detail)

        category_detail_dict.setdefault(category.name, detail_set)

    print("category_detail_dict = " + str(category_detail_dict))
    # category_detail_dict = {'Home/Rent': {'Rent', 'House Loan'}, 'Utilities': {'CellPhone', 'Electricity', 'Water', 'Internet'}, 'Food': {'Dinner', 'Breakfast', 'Fruit', 'Snacks', 'Lunch'}, 'Groceries': {'Necessary', 'Clothes'}, 'Fund money': {''}, 'Entertainment': {'Sport', 'KTV'}, 'Insurance/Medical': {'Insurance', 'Medical'}, 'Travel': {'Taxi', 'Bus', 'Subway'}, 'Salary': {''}}

    return render(request, "finance/show.html",
                  {"categories": categories, "trades": trades, "contents": category_detail_dict})


def main(request):
    if request.method == "POST":
        name = request.POST.get('name')
        status = 0
        result = "OK!"
        return HttpResponse(json.dumps({
            "status": status,
            "result": result
        }))


def index(request):
    # categories = Category.objects.all()
    # trades = Trade.objects.all()
    #
    # # 1. contents: category - details
    # # category_detail_dict = {'Home/Rent': {'Rent', 'House Loan'}, 'Utilities': {'CellPhone', 'Electricity', 'Water', 'Internet'}, 'Food': {'Dinner', 'Breakfast', 'Fruit', 'Snacks', 'Lunch'}, 'Groceries': {'Necessary', 'Clothes'}, 'Fund money': {''}, 'Entertainment': {'Sport', 'KTV'}, 'Insurance/Medical': {'Insurance', 'Medical'}, 'Travel': {'Taxi', 'Bus', 'Subway'}, 'Salary': {''}}
    # category_detail_dict = Utils.queryset_to_set_dict(categories, True)
    #
    # # 2. json serialization; set cannot be serialized -> list
    # # queryset_to_dict_list = [{'id': 1, 'name': 'Home/Rent', 'income': 0.0, 'expense': 8500.0, 'budget': 2000.0}, {'id': 2, 'name': 'Utilities', 'income': 0.0, 'expense': 212.0, 'budget': 2500.0}, {'id': 3, 'name': 'Food', 'income': 0.0, 'expense': 135.0, 'budget': 3000.0}, {'id': 4, 'name': 'Groceries', 'income': 0.0, 'expense': 626.0, 'budget': 3500.0}, {'id': 5, 'name': 'Fund money', 'income': 1000.0, 'expense': 0.0, 'budget': 0.0}, {'id': 6, 'name': 'Entertainment', 'income': 0.0, 'expense': 280.0, 'budget': 1000.0}, {'id': 7, 'name': 'Insurance/Medical', 'income': 0.0, 'expense': 901.0, 'budget': 900.0}, {'id': 8, 'name': 'Travel', 'income': 0.0, 'expense': 23.0, 'budget': 1500.0}, {'id': 9, 'name': 'Salary', 'income': 3000.0, 'expense': 0.0, 'budget': 0.0}]
    # cat_list = Utils.queryset_to_dict_list(categories, True)
    #
    # # 3. expense, income, budget, accounts
    # # bill = {'expenses': 10677.0, 'income': 4000.0, 'budget': 14400.0, 'accounts': -10400.0, 'percent': 74.15, 'remain': 3723.0}
    # bill = Utils.response_data_bill(categories, True)
    #
    # return render(request, "finance/index.html",
    #               {"bill": bill,
    #                "contents": json.dumps(category_detail_dict),
    #                "categories": json.dumps(cat_list),
    #                "bills": json.dumps(bill)})
    return Utils.render_index_page(request, "finance/index.html")

def expense(request):
    # return render(request, "finance/detail.html")
    return Utils.render_index_page(request, "finance/expense.html")


def home_detail(request):
    # return render(request, "finance/homeDetail.html")
    return Utils.render_index_page(request, "finance/homeDetail.html")


def utilities_detail(request):
    # return render(request, "finance/UtilitiesDetail.html")
    return Utils.render_index_page(request, "finance/UtilitiesDetail.html")


def add_detail(request):
    # return render(request, "finance/UtilitiesDetail.html")
    return Utils.render_index_page(request, "finance/addDetail.html")


# AJAX POST
def add_category(request):
    name = request.POST.get("name")
    budget = request.POST.get("budget")

    category = Category()
    category.name = name
    category.budget = budget
    category.save()

    return JsonResponse({"res": 1})


def remove_category(request):
    catogory_id = request.POST.get("id")

    # 删除数据库中对应的记录
    trades = Trade.objects.filter(id=catogory_id)
    trades.delete()
    category = Category.objects.get(id=catogory_id)
    category.delete()

    return JsonResponse({"res": 1})


# def add_detail_trade(request):
#     type = request.POST.get("type")
#     category_name = request.POST.get("category_name")
#     detail = request.POST.get("detail")
#     trade_date = request.POST.get("trade_date")
#     remark = request.POST.get("remark")
#     price = request.POST.get("price")
#
#     trade = Trade()
#     trade.type = type
#     trade.detail = detail
#     trade.trade_date = trade_date
#     trade.remark = remark
#     trade.price = price


def add_trade(request):
    # 1.判断请求方式
    # if request.method == 'POST':
    # 2. 获取表单提交过来的数据
    type = request.POST.get('type')
    detail = request.POST.get('detail')
    price = request.POST.get('price')
    trade_date = request.POST.get('trade_date')
    remark = request.POST.get('remark')
    category_name = request.POST.get('category_name')

    category = Category.objects.get(name=category_name)

    trade = Trade()
    trade.type = False if type == "0" else True
    trade.detail = detail
    trade.trade_date = trade_date
    trade.remark = remark
    trade.price = float(price)
    trade.category = category
    print("type" + str(trade))

    if trade.type is False: # expense
        category.expense += float(trade.price)
    else: # income
        category.income += float(trade.price)
    trade.save()
    category.save()

    return JsonResponse({"res": 1})


def remove_trade(request):
    category_name = request.POST.get("category_name")
    detail = request.POST.get("detail")

    category = Category.objects.get(name=category_name)
    trades = Trade.objects.filter(detail=detail, category=category)
    income, expense = 0.0, 0.0
    for trade in trades:
        if trade.type is True:
            income += trade.price
        else:
            expense += trade.price
    category.income -= income
    category.expense -= expense
    category.save()

    trades.delete()

    return JsonResponse({"res": 1})


def import_data(request):
    return render(request, "finance/import.html")
