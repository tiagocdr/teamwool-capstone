"""woolnews_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from woolnews_app.views import AboutView, ContactView, fav_post, PostDeleteView
# from discussion.views import DiscussionView
from woolnews_app import views
# from discussion.views import DiscussionView
from discussion.views import create_discussion, discussion_view, like_comment_forum, fav_forum
from django.conf import settings
from django.conf.urls.static import static
from userauth.views import UserEditView, ProfileView
from userauth.urls import urlpatterns as user_urls
from genres.urls import urlspatterns as genres_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    # General views 
    path('', views.home_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    #Post views
    path('create/', views.create_post, name='create'),
    path('delete_post/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    # path('postlike/<int:post_id>', views.like_post, name='like post'),
    path('post/<int:post_id>', views.post_view, name='post view'),
    path('favpost/<int:post_id>', views.fav_post, name='fav post'),
    #Forum Views
    path('forum/<int:forum_id>', discussion_view, name='forum-details'),
    path('createforum/<int:post_id>', create_discussion, name='create forum'),
    path('favforum/<int:forum_id>', fav_forum, name='fav forum'),
    # Comment Views
    path('commentlike/<int:comment_id>', views.like_comment, name='like comment'),
    path('commentlikeforum/<int:comment_id>', like_comment_forum, name='like comment forum'),
    # Imports
    path('accounts/', include('userauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] 

urlpatterns = urlpatterns + user_urls + genres_urls
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
