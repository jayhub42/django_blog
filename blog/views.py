from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from comments.forms import CommentForm
# Create your views here.


def index(request):
    comment_form = CommentForm()
    latest_article = Article.objects.filter(published_bool=True).order_by('-published_on_date')
    context = {'article': latest_article,'comment_form': comment_form}
    return render(request, 'blog/welcome.html', context)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article.html', {'article': article})

