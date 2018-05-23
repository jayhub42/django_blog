from django.forms import ModelForm
from .models import Comment
# Create your views here.


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['blog', "body_str", 'author']