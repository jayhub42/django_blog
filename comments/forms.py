from django.forms import ModelForm
from .models import Comment
# Create your views here.


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body_str"]