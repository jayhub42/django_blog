from django.shortcuts import render
from .models import Article
# Create your views here.


def index(request):
    latest_article = Article.objects.filter(published_bool=True).order_by('-published_on_date')
    context = {'article': latest_article}
    return render(request, 'blog/welcome.html', context)
