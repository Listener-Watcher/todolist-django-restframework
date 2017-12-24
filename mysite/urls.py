from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from todolist import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UserSystem.views.home', name='home'),
    url(r'^accounts/profile/$', 'UserSystem.views.profile', name='profile'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^todolist/$', 'todolist.views.board', name='todolist'),
    url(r'^todolist/details/(?P<id>\w{0,50})/$', 'todolist.views.details'),
    url(r'^todolist/add/$', 'todolist.views.add', name='add'),
    url(r'^board/$', 'todolist.views.board', name='board'),
    url(r'^todolist/deletion/(?P<id>\w{0,50})/$', 'todolist.operations.delete'),
    url(r'^todolist/finished/(?P<id>\w{0,50})/$', 'todolist.operations.finished'),
    url(r'^todolist/edition/(?P<id>\w{0,50})/$', 'todolist.operations.edit', name='edit'),
    url(r'^todolist/api/$', views.ItemList.as_view()),
    url(r'^todolist/api/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
]