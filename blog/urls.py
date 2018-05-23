from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:article_id>/', views.article, name='detail'),
    path('', views.index, name='index'),
    # re_path(r'^.*', views.index),
]