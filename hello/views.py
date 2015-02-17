from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from hello.models import Article, Comment
from hello import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView


class ArticleList(TemplateView):

    def get(self, request, *args, **kwargs):
        all_articles = Article.objects.order_by('-id')
        paginator = Paginator(all_articles, 3)
        page = request.GET.get('page')
        try:
            paged_articles = paginator.page(page)
        except PageNotAnInteger:
            paged_articles = paginator.page(1)
        except EmptyPage:
            paged_articles = paginator.page(paginator.num_pages)
        return render(request, 'list.html', {'articles': paged_articles})


class ArticleView(TemplateView):

    def get(self, request, article_id='0', *args, **kwargs):
        comment_form = forms.AddComment()
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'single.html', {'article': article,
                                               'comment_form': comment_form})

    def post(self, request, article_id='0'):
        comment_form = forms.AddComment(request.POST)
        article = get_object_or_404(Article, id=article_id)
        if comment_form.is_valid():
            comment = Comment()
            comment.body = comment_form.cleaned_data['body']
            comment.username = comment_form.cleaned_data['user_name']
            comment.parent_comment = request.POST['comment_parent_id']
            # input field comment_parent_id is generating by javascript in reply action
            comment.article = article
            comment.save()
            return HttpResponseRedirect('/article/' + article_id)
        else:
            comment_form = forms.AddComment()

        return render(request, 'single.html', {'article': article,
                                               'comment_form': comment_form})


class ArticleManage(TemplateView):

    def get(self, request, *args, **kwargs):
        form = forms.AddPost()
        return render(request, 'addpost.html', {'form': form})

    def put(self, request):
        form = forms.AddPost(request.PUT)
        if form.is_valid():
            savedTitle = form.cleaned_data['title']
            savedBody = form.cleaned_data['body']
            savePost = Article(title=savedTitle, body=savedBody)
            savePost.save()
            return render(request, 'thank.html')
        else:
            form = forms.AddPost()
        return render(request, 'addpost.html', {'form': form})

    def post(self, request):
        article_id = request.POST['article_id']
        articleToRemove = get_object_or_404(Article, id=article_id)
        articleToRemove.delete()
        return HttpResponseRedirect('/')

