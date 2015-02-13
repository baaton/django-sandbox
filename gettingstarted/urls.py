from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.views import list_all, blogadmin, thanks, one, delete_article

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', list_all),
    url(r'^article/(?P<article_id>\d+)/$', one),
    url(r'^delete/(?P<article_id>\d+)/$', delete_article),
    url(r'^article/$', list_all),
    url(r'^blogadmin/$', blogadmin),
    url(r'^thanks/$', thanks),
)