from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Article

def list(request, articleid=0):
    # return HttpResponse(Article.objects.all()[0].title)
    if articleid==0:
        return render(request, 'articles.html', {'articles': Article.objects.all()})
    else:
        return render(request, 'articles.html', {'articles': Article.objects.all()[int(articleid)-1], 'articleid': articleid})