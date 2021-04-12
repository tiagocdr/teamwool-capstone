from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
           
            'first_name',
            'last_name'
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
           
            'first_name',
            'last_name'
        )

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = {'email', 'first_name', 'last_name', 'img', 'bio'}