from django import forms


class DiscussionForm(forms.Form):
    title = forms.CharField(max_length=140)
    body = forms.CharField(widget=forms.Textarea)