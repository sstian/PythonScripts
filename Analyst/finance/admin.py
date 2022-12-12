from django.contrib import admin
from finance.models import Category, Trade


class CategoryAdmin(admin.ModelAdmin):

   list_display = ["id", "name", "income", "expense", "budget"]


class TradeAdmin(admin.ModelAdmin):

    list_display = ["id", "type", "detail", "price", "trade_date", "remark", "category_id"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Trade, TradeAdmin)
