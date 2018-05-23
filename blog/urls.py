from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article, name='detail'),
    # re_path(r'^.*', views.index),
]