
from typing import Generator
from django.db.models import query
from django.http import request
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from woolnews_app.models import CommentModel, PostModel
from favorites.models import FavoritesModel
from woolnews_app.forms import PostForm, CommentForm


# This is a hack
def get_most_faved_post(queryset):
    obj = queryset.first()
    counter = (0, obj)
    for f in queryset:
        curr_post = (0, f.post)
        if counter[1] is not curr_post[1]:
            counter = curr_post
        counter[0] + 1

    return counter[1] 
    

def home_view(request):
    posts = PostModel.objects.all()
    favorites = FavoritesModel.objects.all()
    featured_post = get_most_faved_post(favorites)
    context = {
            'object_list': posts,
            'featured_post': featured_post
            }
    return render(request, 'news.html', context)


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
    favorite = FavoritesModel.objects.create(  
    user=request.user,
    post=post
    )
    favorite.save()
    post.favs.add(favorite)
    return redirect('post view', post_id=post.id)


def post_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    comments_form = CommentForm()
    comments = post.comments.all().order_by('-timestamp')
    favs = FavoritesModel.objects.filter(post=post)
    # Check if user faved it.
    is_faved = None
    if request.user.is_authenticated:
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
            print(data)
            post = PostModel.objects.create(
                title=data['title'],
                body=data['body'],
                user=request.user,
                img=data['img'],
                genre=data['genre']
            )
            return redirect('post view', post_id=post.id)

    form = PostForm()
    return render(
        request,
        'post-form.html',
        {'form': form}
    )

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = PostModel

    success_url ="/"
