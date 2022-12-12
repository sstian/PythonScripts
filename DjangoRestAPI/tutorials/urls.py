from django.conf.urls import url
from tutorials import views

# Methods	Urls	Actions
# GET	api/tutorials	get all Tutorials
# GET	api/tutorials/:id	get Tutorial by id
# POST	api/tutorials	add new Tutorial
# PUT	api/tutorials/:id	update Tutorial by id
# DELETE	api/tutorials/:id	remove Tutorial by id
# DELETE	api/tutorials	remove all Tutorials
# GET	api/tutorials/published	find all published Tutorials
# GET	api/tutorials?title=[kw]	find all Tutorials which title contains 'kw'

# /api/tutorials: GET, POST, DELETE
# /api/tutorials/:id: GET, PUT, DELETE
# /api/tutorials/published: GET

# tutorial_list(): GET list of tutorials, POST a new tutorial, DELETE all tutorials
# tutorial_detail(): GET / PUT / DELETE tutorial by ‘id’
# tutorial_list_published(): GET all published tutorials

urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published)
]

