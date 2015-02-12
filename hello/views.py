from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Article

def list(request):
    # return HttpResponse(Article.objects.all()[0].title)
    return render(request, 'home.html', {'articles': Article.objects.all()})