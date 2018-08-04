from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from blog.models import Article
from .forms import CommentForm


@login_required
def index(request, article_id):
    # latest_article = Article.objects.filter(published_bool=True).order_by('-published_on_date')
    # context = {'article': latest_article}
    # return render(request, 'blog/welcome.html', context)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.author = request.user
        latest_article = Article.objects.only('id').get(id=article_id)
        comment.blog = latest_article
        comment.save()
        comment_form = CommentForm()
        context = {'article': latest_article, 'comment_form': comment_form}
        return render(request, 'blog/article.html', context)
    else:
        latest_article = Article.objects.filter(published_bool=True, pk=article_id)
        context = {'article': latest_article, 'comment_form': comment_form}
        return render(request, 'blog/article.html', context)
