from favorites.models import FavoritesModel
from woolnews_app.models import PostModel
from django.shortcuts import redirect, render
# from django.views.generic import ListView, DetailView, CreateView
from .models import DiscussionModel
from .forms import DiscussionForm
from woolnews_app.models import PostModel, CommentModel
from woolnews_app.forms import CommentForm
# Create your views here.


# for sake of simplicity and flexibility  reformated the class view to a function 
# TODO: Implement comments in discussions, likes, link to the post and closing options

def like_comment_forum(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    comment.votes += 1
    comment.save()
    user = comment.user
    discussion = DiscussionModel.objects.get(user=user, comments=comment)
    return redirect('forum-details', forum_id=discussion.id)

def fav_forum(request, forum_id):
    discussion = DiscussionModel.objects.get(id=forum_id)
    model = FavoritesModel.objects.filter(user=request.user,discussion=discussion)
    if model:
        model.delete()
        return redirect('forum-details', forum_id=discussion.id)
    favorite = FavoritesModel.objects.create(  
        user=request.user,
        discussion=discussion
    )
    favorite.save()
    discussion.favs.add(favorite)
    return redirect('forum-details', forum_id=discussion.id)


def discussion_view(request, forum_id):
    discussion = DiscussionModel.objects.get(id=forum_id)
    form = CommentForm()
    comments = discussion.comments.all().order_by('-timestamp')
    favs = FavoritesModel.objects.filter(discussion=discussion)
    # Check if user faved it.
    is_faved = FavoritesModel.objects.filter(user=request.user, discussion=discussion)
    context = {
        'discussion':discussion,
        'form': form,
        'comments': comments,
        'favs': len(favs),
        'is_faved': is_faved
        }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            discussion.comments.create(
                user=request.user,
                text=data['text']
                )
    return render(request, 'forum.html',context)


def create_discussion(request, post_id):
    post = PostModel.objects.get(id=post_id)
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            forum = post.discussion.create(
                user=request.user,
                title=data['title'],
                body=data['body'],
                post=post
                )
            return redirect('forum-details', forum_id=forum.id)
    form = DiscussionForm()
    return render(request,'forum-form.html', {'form': form})