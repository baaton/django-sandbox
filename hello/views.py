from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from hello.models import Article, Comment
from hello import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime


def one(request, article_id='0'):
    """ View a post """
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        comment_form = forms.AddComment(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.body = comment_form.cleaned_data['body']
            comment.username = comment_form.cleaned_data['user_name']
            comment.parent_comment = request.POST['comment_parent_id']
            # инпут comment_parent_id генерится javascript и не передается в объекте
            comment.article = article
            comment.save()
            return HttpResponseRedirect('/article/' + article_id)
    else:
        comment_form = forms.AddComment()

    return render(request, 'single.html', {'article': article,
                                           'comment_form': comment_form})


def list_all(request, page=1):
    """ Show all posts """
    all_articles = Article.objects.order_by('-id')
    paginator = Paginator(all_articles, 3)
    page = request.GET.get('page')
    try:
        paged_articles = paginator.page(page)
    except PageNotAnInteger:
        paged_articles = paginator.page(1)
    except EmptyPage:
        paged_articles = paginator.page(paginator.num_pages)
    return render(request,
                  'list.html',
                  {'articles': paged_articles})


def blogadmin(request, article_id=0):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            savedTitle = form.cleaned_data['title']
            savedBody = form.cleaned_data['body']
            savePost = Article(title=savedTitle,
                               body=savedBody)
            savePost.save()
            return render(request, 'thank.html')
    else:
        form = forms.AddPost()
    return render(request, 'addpost.html', {'form': form})


def delete_article(request, article_id=0):
    articleToRemove = get_object_or_404(Article, id=article_id)
    articleToRemove.delete()
    return HttpResponseRedirect('/')


def thanks(request):
    return HttpResponse('Thank you! We add your article to database.')