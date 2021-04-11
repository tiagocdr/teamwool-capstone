from typing import Generator

from django.http import request
from woolnews_app.models import PostModel
from django.views.generic import ListView, DetailView, CreateView
from woolnews_app.forms import PostForm
from django.shortcuts import render, redirect
from .forms import PostForm

# TODO: Post View
class  HomeView(ListView):
    model = PostModel
    template_name = 'news.html'

# TODO: Post View

# TEMP Home/News list view
# def home_view(request):
#     return render(
#         request,
#         'news.html',
#         {}
#     )
class ForumView(DetailView):
    model = PostModel
    template_name = 'forum.html'
# TEMP Forum list view
# def forum_view(request):
#     return render(
#         request,
#         'forum.html',
#         {}
#     )


class AddBlogView(CreateView):
    model = PostModel
    template_name = 'post-form.html'
    fields = '__all__'


class AboutView(ListView):
    model = PostModel
    template_name = 'about.html'
    
# TEMP About view
# def about_view(request):
#     return render(
#         request,
#         'about.html',
#         {}
#     )


class ContactView(ListView):
    model = PostModel
    template_name = 'contact.html'
# TEMP Contact view
# def contact_view(request):
#     return render(
#         request,
#         'contact.html',
#         {}
#     )
    
    
class ProfileView(DetailView):
    model = PostModel
    template_name = 'profile.html'


def CreatePostView(request):
    pass