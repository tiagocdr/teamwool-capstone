from django import forms
from woolnews_app.models import PostModel
# TODO: Post Form, Comment Form.

class PostForm(forms.ModelForm):
    class Meta:
        model= PostModel
        fields = ['title','img', 'body','genre']
    # title = forms.CharField(max_length=100)
    # img = forms.ImageField()
    # body = forms.CharField(max_length=1000, widget=forms.Textarea)
    # genre = forms.CharField()

class CommentForm(forms.Form):
    text = forms.CharField(max_length=240)
