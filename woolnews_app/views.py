from django.shortcuts import render


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
