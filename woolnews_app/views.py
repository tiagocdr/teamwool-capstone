
from typing import Generator
from django.http import request
from woolnews_app.models import CommentModel, PostModel
from favorites.models import FavoritesModel
from django.views.generic import ListView, DetailView, CreateView
from woolnews_app.forms import PostForm, CommentForm
from django.shortcuts import render, redirect

# TODO: Post View
class  HomeView(ListView):
    model = PostModel
    template_name = 'news.html'


class AboutView(ListView):
    model = PostModel
    template_name = 'about.html'
    
# TEMP About view


class ContactView(ListView):
    model = PostModel
    template_name = 'contact.html'
# TEMP Contact view

def like_comment(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    comment.votes += 1
    comment.save()
    user = comment.user
    post = PostModel.objects.get(user=user, comments=comment)
    return redirect('post view', post_id=post.id)


def fav_post(request, post_id):
    post = PostModel.objects.get(id=post_id)
    model = FavoritesModel.objects.filter(user=request.user,post=post)
    if model:
        model.delete()
        return redirect('post view', post_id=post.id)
    FavoritesModel.objects.create(  
    user=request.user,
    post=post
    )
    return redirect('post view', post_id=post.id)


def post_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    comments_form = CommentForm()
    comments = post.comments.all().order_by('-timestamp')
    favs = FavoritesModel.objects.filter(post=post)
    # Check if user faved it.
    is_faved = FavoritesModel.objects.filter(user=request.user, post=post)
    context = {
        'post': post,
        'form':comments_form,
        'comments': comments,
        'lenght': len(comments),
        'favs': len(favs),
        'is_faved': is_faved
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
                user=request.user,
                img=data['img']
            )
            return redirect('post view', post_id=post.id)

    form = PostForm()
    return render(
        request,
        'post-form.html',
        {'form': form}
    )

