from django.urls import path, re_path

from . import views

urlpatterns = [
    path('<int:article_id>/', views.index, name='index'),
    # re_path(r'^.*', views.index),
]