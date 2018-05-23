import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from blog import models
# Create your models here.


class Comment(models.Model):
    blog = models.ForeignKey(models.Article)
    body_str = models.TextField("Comment")
    created_on_datetime = models.DateTimeField('Created at', auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete='PROTECTED')

    def __str__(self):
        return self.author

