
# 自定义中间件类
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class TestMiddleware(MiddlewareMixin):

    EXCLUDE_IPS = ["192.168.1.1"]

    def __init__(self, get_response=None):
        super().__init__(get_response)
        print("TestMiddleware.__init__()")

    def process_request(self, request):
        print("TestMiddleware.process_request()")

    def process_view(self, request, view_func, *args, **kwargs):
        print("TestMiddleware.process_view()")
        user_ip = request.META["REMOTE_ADDR"]
        print("user_ip = " + user_ip)
        if user_ip in self.EXCLUDE_IPS:
            return HttpResponse("<h1>Forbidden<h1>")

    def process_response(self, request, response):
        print("TestMiddleware.process_response()")
        return response

    def process_exception(self, request, exception):
        print("TestMiddleware.process_exception()")