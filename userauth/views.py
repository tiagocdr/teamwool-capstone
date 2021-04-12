from django.views.generic.detail import DetailView
from woolnews_app.models import PostModel
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserChangeForm
from woolnews_app.forms import PostForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from woolnews_app.models import Profile
# SignUp View


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    
class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    
    
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user
   

