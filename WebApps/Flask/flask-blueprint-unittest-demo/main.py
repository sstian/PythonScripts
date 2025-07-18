from flask import Flask, request, jsonify
from cart import app_cart

# 创建flask的应用对象
# __name__ 如果文件作为启动模块则为"__main__"，如果文件作为模块被导入则为文件标题
# flask以这个模块所在的目录为启动目录，如果未找到则以该文件所在的目录为启动目录，
# 默认：这个目录中的static为静态目录，templates为模板目录
app = Flask(__name__)

# 配置参数
class Config(object):
    DEBUG = True

app.config.from_object(Config)

# 注册蓝图
app.register_blueprint(app_cart, url_prefix="/cart")

# 路由和视图函数
@app.route("/")
def index():
    """定义视图函数"""
    return "index page"

@app.route("/login", methods=["GET", "POST"])
def login():
    # 接收参数
    username = request.form.get("username")
    password = request.form.get("password")

    # 参数判断
    if not all([username, password]):
        response = { "code": 1, "message": "invalid params" }
        return jsonify(response)
    if username == "admin" and password == "python":
        response = { "code": 0, "message": "login success" }
        return jsonify(response)
    else:
        response = { "code": 2, "message": "wrong username or password" }
        return jsonify(response)

if __name__ == "__main__":
    print(app.url_map)
    # app.run(debug=True)
    app.run()
