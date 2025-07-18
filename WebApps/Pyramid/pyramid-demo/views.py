from html import escape

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


# First view, available at http://localhost:6543/
@view_config(route_name='home')
def home_view(request):
    return Response('<p>Visit <a href="/howdy/lisa">hello</a></p>')


# # /howdy?name=alice which links to the next view
# @view_config(route_name='hello')
# def hello_view(request):
#     name = request.params.get('name', 'No Name')
#     body = '<p>Hi %s, this <a href="/goto">redirects</a></p>'
#     # Python html.escape to prevent Cross-Site Scripting (XSS) [CWE 79]
#     return Response(body % escape(name))


# @view_config(route_name='hello', renderer='hello_world.pt')
# def hello_world(request):
#     return dict(name=request.matchdict['name'])

@view_config(route_name='hello', renderer='hello_world.jinja2')
def hello_world(request):
    return dict(name=request.matchdict['name'])

# /goto which issues HTTP redirect to the last view
@view_config(route_name='redirect')
def redirect_view(request):
    return HTTPFound(location="/problem")


# /problem which causes a site error
@view_config(route_name='exception')
def exception_view(request):
    raise Exception()

# 返回json
@view_config(route_name='hello_json', renderer='json')
def hello_json(request):
    return [1, 2, 3]
