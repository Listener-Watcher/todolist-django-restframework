from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'todolist'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^details/(?P<id>\w{0,50}/$)',views.details),
	url(r'^add/$',views.add),
	url(r'^api/$',views.ItemList.as_view()),
	url(r'^api/(?P<id>\w{0,50}/$',views.ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)