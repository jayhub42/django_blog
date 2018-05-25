from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from comments.models import Comment
from comments.forms import CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    comment_form = CommentForm()
    latest_article = Article.objects.filter(published_bool=True).order_by('-published_on_date')
    context = {'article': latest_article,'comment_form': comment_form}
    return render(request, 'blog/welcome.html', context)

@login_required
def article(request, article_id):
    article_rec = get_object_or_404(Article, pk=article_id)
    comments_rec = article_rec.comment_set.all()
    # article_rec = Article.objects.all()
    comment_form = CommentForm(initial={'body_str': "hello",'blog':article_id})
    print("article rec", article_rec)
    print("comments", comments_rec)
    return render(request, 'blog/article.html', {'article': article_rec, "comment_form": comment_form,
                                                 'comments': comments_rec})

