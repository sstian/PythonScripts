from flask import Blueprint

# 创建蓝图
app_cart = Blueprint("app_cart", __name__, template_folder="templates", static_folder="static")

# 加载视图
from .views import get_cart
