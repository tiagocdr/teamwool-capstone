from django import forms
from woolnews_app.models import PostModel
# TODO: Post Form, Comment Form.

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    img = forms.ImageField()
    body = forms.CharField(max_length=1000, widget=forms.Textarea)

class CommentForm(forms.Form):
    text = forms.CharField(max_length=240)
