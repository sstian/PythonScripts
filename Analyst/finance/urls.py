
from django.contrib import admin
from django.urls import path, re_path
from finance import views

urlpatterns = [
    path('', views.home),
    re_path(r"^show$", views.show),
    re_path(r"^main$", views.main),
    re_path(r"^index", views.index),
    re_path(r"^expense", views.expense),
    re_path(r"^homeDetail", views.home_detail),
    re_path(r"^UtilitiesDetail", views.utilities_detail),

    re_path(r"^addCategory", views.add_category),
    re_path(r"^removeCategory", views.remove_category),
    re_path(r"^addDetail", views.add_detail),
    re_path(r"^addTrade", views.add_trade),
    re_path(r"^removeTrade", views.remove_trade),
    re_path(r"^import", views.import_data),

]
