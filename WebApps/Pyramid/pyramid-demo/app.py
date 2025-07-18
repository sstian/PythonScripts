

# 解决警告：
# D:\Program\Python\Python313\Lib\site-packages\pyramid\asset.py:2: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
# import pkg_resources
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pyramid.asset")


from wsgiref.simple_server import make_server
from pyramid.config import Configurator


if __name__ == '__main__':
    with Configurator() as config:
        # 添加路由映射
        config.add_route('home', '/')
        # config.add_route('hello', '/howdy')
        # config.add_route('hello', '/howdy/{first}/{last}')
        config.add_route('hello', '/howdy/{name}')
        config.add_route('redirect', '/goto')
        config.add_route('exception', '/problem')
        config.add_route('hello_json', 'hello.json')
        
        # 使用模板渲染器
        config.include('pyramid_chameleon')
        config.include('pyramid_jinja2')

        config.scan('views')
        app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
