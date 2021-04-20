from django import forms
from woolnews_app.models import PostModel


# TODO: Post Form, Comment Form.

# News draft form
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'img', 'body', 'genre', 'sources']

# Comment form
class CommentForm(forms.Form):
    comment = forms.CharField(max_length=240)
