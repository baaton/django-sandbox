from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from hello.models import Article
from hello import forms

def list(request, articleid=0):
    # return HttpResponse(Article.objects.all()[0].title)
    if articleid==0:
        return render(request, 'articles.html', {'articles': Article.objects.order_by("-id")})
    else:
        return render(request, 'articles.html', {'articles': Article.objects.all()[int(articleid)-1], 'urlarticleid': articleid})

def blogadmin(request):
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

def thanks(request):
    return HttpResponse('Thank you! We add your article to database.')