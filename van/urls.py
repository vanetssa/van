from django.conf.urls import patterns, include, url
from van.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'van.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
	url(r'^$',index)
)
