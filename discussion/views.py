from woolnews_app.models import PostModel
from django.shortcuts import redirect, render
# from django.views.generic import ListView, DetailView, CreateView
from .models import DiscussionModel
from .forms import DiscussionForm
from woolnews_app.models import PostModel
# Create your views here.


# for sake of simplicity and flexibility  reformated the class view to a function 
# TODO: Implement comments in discussions, likes, link to the post and closing options
def discussion_view(request, forum_id):
    discussion = DiscussionModel.objects.get(id=forum_id)
    return render(request, 'forum.html',{'discussion':discussion})

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
                )
            return redirect('forum-details', forum_id=forum.id)
    form = DiscussionForm()
    return render(request,'forum-form.html', {'form': form})