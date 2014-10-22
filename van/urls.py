from django.conf.urls import patterns,url
from van.views import index,blog,community

urlpatterns = patterns('',
    # url(r'^$', 'van.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',index),
    url(r'^blog$',blog),
    url(r'^community$',community)
)