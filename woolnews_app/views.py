from woolnews_app.models import PostModel
from woolnews_app.forms import PostForm
from django.shortcuts import render, redirect
from .forms import PostForm

# TODO: Post View

# TEMP Home/News list view
def home_view(request):
    return render(
        request,
        'news.html',
        {}
    )


# TEMP Forum list view
def forum_view(request):
    return render(
        request,
        'forum.html',
        {}
    )


# TEMP About view
def about_view(request):
    return render(
        request,
        'about.html',
        {}
    )


# TEMP Contact view
def contact_view(request):
    return render(
        request,
        'contact.html',
        {}
    )

def post_view(request, post_id):
    post = PostModel.objects.get(id=post_id)
    print(dir(post.img), post.img)
    return render(request, 'post.html', {'post': post})

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