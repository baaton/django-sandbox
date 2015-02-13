from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from hello.models import Article
from hello import forms


def one(request, article_id=0):
    """ View a post """
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'single.html', {'article': article, 'articles': []})


def list_all(request):
    """ Show all posts """
    return render(request,
                  'list.html',
                  {'articles': Article.objects.order_by('-id')})


def blogadmin(request, article_id=0):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            savedTitle = request.POST.get("title")
            savedBody = request.POST.get("body")
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