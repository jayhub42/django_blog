import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    body_str = models.TextField("body")
    title = models.CharField('Title', max_length=255, unique=True)
    created_on_datetime = models.DateTimeField('Created at', auto_now_add=True, editable=False)
    published_on_date = models.DateTimeField('Published at', null=True, blank=True)
    published_bool = models.BooleanField("Published", default=False)
    author = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete='PROTECTED')

    def was_published_recently(self):
        return self.published_on_date >= timezone.now() - datetime.timedelta(days=1)

    # def __str__(self):
    #     return self.title
