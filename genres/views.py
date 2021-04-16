from django.shortcuts import render
from woolnews_app.models import PostModel
# Create your views here.

# Not quite DRY...

def automotive_view(request):
    posts = PostModel.objects.filter(genre='AT')
    context = {'posts': posts}
    return render(request, 'genres.html', context)


def sports_view(request):
    posts = PostModel.objects.filter(genre='SP')
    context = {'posts': posts}
    return render(request, 'genres.html', context)


def arts_view(request):
    posts = PostModel.objects.filter(genre='AR')
    context = {'posts': posts}
    return render(request, 'genres.html', context)


def cc_view(request):
    posts = PostModel.objects.filter(genre='CC')
    context = {'posts': posts}
    return render(request, 'genres.html', context)


def dadjokes_view(request):
    posts = PostModel.objects.filter(genre='DJ')
    context = {'posts': posts}
    return render(request, 'genres.html',context)
    

def opinion_view(request):
    posts = PostModel.objects.filter(genre='OP')
    context = {'posts': posts}
    return render(request, 'genres.html', context)


def politics_view(request):
    posts = PostModel.objects.filter(genre='PL')
    context = {'posts': posts}
    return render(request, 'genres.html', context)
