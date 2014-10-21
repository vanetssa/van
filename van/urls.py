from django.conf.urls import patterns, url
from van.views import index,pull

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'van.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',index),
	url(r'^pull$',pull)
)