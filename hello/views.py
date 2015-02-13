from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from hello.models import Article, Comment
from hello import forms
import datetime


def one(request, article_id=0):
    """ View a post """
    if request.method == 'POST':
        comment_form = forms.AddComment(request.POST)
        if comment_form.is_valid():
            saved_username = comment_form.cleaned_data['user_name']
            saved_body = comment_form.cleaned_data['body']
            save_comment = Comment(article_id=article_id,
                                  parent_id=0,
                                  date=datetime.datetime.now(),
                                  user_name=saved_username,
                                  body=saved_body)
            save_comment.save()
            return HttpResponseRedirect('/article/' + article_id)
    else:
        comment_form = forms.AddComment()

    article = get_object_or_404(Article, id=article_id)
    article_comments = Comment.objects.filter(article_id=article_id).order_by('-id')

    return render(request, 'single.html', {'article': article,
                                           'comment_form': comment_form,
                                           'comments': article_comments})


def list_all(request):
    """ Show all posts """
    return render(request,
                  'list.html',
                  {'articles': Article.objects.order_by('-id')})


def blogadmin(request, article_id=0):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            savedTitle = form.cleaned_data['title']
            savedBody = form.cleaned_data['body']
            savePost = Article(title=savedTitle, body=savedBody)
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