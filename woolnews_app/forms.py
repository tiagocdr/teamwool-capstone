from django import forms
from woolnews_app.models import PostModel


# TODO: Post Form, Comment Form.

# News draft form
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'img', 'body', 'genre']
    # title = forms.CharField(max_length=100)
    # img = forms.ImageField()
    # body = forms.CharField(max_length=1000, widget=forms.Textarea)
    # genre = forms.CharField()


# Comment form
class CommentForm(forms.Form):
    comment = forms.CharField(max_length=240)
