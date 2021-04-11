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
from django.contrib import admin
from django.urls import path, include
from woolnews_app.views import HomeView, ForumView, AboutView, ContactView, AddBlogView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', HomeView.as_view(), name='home'),
    path('forum/<int:pk>', ForumView.as_view(), name='forum-details'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', AddBlogView.as_view(), name='create-post'),
    # path('profile/', ProfileView, name='profile'),
=======
    path('', views.home_view, name='home'),
    path('forum/', views.forum_view, name='forum'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('create/', views.create_post, name='create'),
    path('post/<int:post_id>', views.post_view, name='post view'),
>>>>>>> 6cca6f905b4925619fd7fa4bcef50e142bdd3c63
    path('accounts/', include('userauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)