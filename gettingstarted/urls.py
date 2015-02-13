from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.views import list, blogadmin, thanks

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list),
    url(r'^article/(?P<articleid>\d+)/$', list),
    url(r'^article/$', list),
    url(r'^blogadmin/$', blogadmin),
    url(r'^thanks/$', thanks),
)