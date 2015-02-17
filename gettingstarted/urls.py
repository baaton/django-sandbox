from django.conf.urls import patterns, include, url
from django.contrib import admin
from hello.views import ArticleList, ArticleView, ArticleManage

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ArticleList.as_view()),
    url(r'^article/$', ArticleList.as_view()),
    url(r'^article/(?P<article_id>\d+)/$', ArticleView.as_view()),
    url(r'^addarticle/$', ArticleManage.as_view(), name="add-article")
)