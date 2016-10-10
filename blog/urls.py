from django.conf.urls import url

from . import views
'''
Add a URL to urlpatterns:  url(r'^$', views.index, name = 'index'),
'''

urlpatterns = [
	
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<blogid>[0-9]+)/$', views.details, name='blogid'),
]