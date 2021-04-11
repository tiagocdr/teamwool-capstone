<<<<<<< HEAD
from typing import Generator

from django.http import request
from woolnews_app.models import PostModel
from django.views.generic import ListView, DetailView, CreateView
from woolnews_app.forms import PostForm
=======
from woolnews_app.models import PostModel, CommentModel
from woolnews_app.forms import PostForm, CommentForm
>>>>>>> 6cca6f905b4925619fd7fa4bcef50e142bdd3c63
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
<<<<<<< HEAD
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
=======
def contact_view(request):
    return render(
        request,
        'contact.html',
        {}
    )

def post_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    comments_form = CommentForm()
    comments = post.comments.all().order_by('-timestamp')
    context = {
        'post': post,
        'form':comments_form,
        'comments': comments,
        'lenght': len(comments)
        }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.comments.create(
                user=request.user,
                text=data['text']
                )
            return redirect('post view', post_id=post.id)
    return render(request, 'post.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            post = PostModel.objects.create(
                title=data['title'],
                body=data['body'],
                user=request.user
            )
            return redirect('post view', post_id=post.id)

    form = PostForm()
    return render(
        request,
        'post-form.html',
        {'form': form}
    )
>>>>>>> 6cca6f905b4925619fd7fa4bcef50e142bdd3c63
