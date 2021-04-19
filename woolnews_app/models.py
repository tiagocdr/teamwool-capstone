from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from discussion.models import DiscussionModel
from userauth.models import CustomUser
from django.urls import reverse
# TODO: Automatically default to a general genre if not provided one.


class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    timestamp = models.TimeField(default=timezone.now)
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.text} | {self.user}'



class PostModel(models.Model):
    AUTOMOTIVE = 'AT'
    SPORTS = 'SP'
    ARTS = 'AR'
    POLITICS = 'PL'
    CLIMATE_CHANGE = 'CC'
    OPINION = 'OP'
    DAD_JOKES = 'DJ'
    GENERAL = 'GEN'

    CHOICES = [
        (AUTOMOTIVE, 'Automotive'),
        (SPORTS, 'Sports'),
        (ARTS, 'Arts'),
        (POLITICS, 'Politics'),
        (CLIMATE_CHANGE, 'Climate Change'),
        (OPINION, 'Opinion'),
        (DAD_JOKES, 'DadJokes'),
        (GENERAL, 'General'),
    ]

    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.TimeField(default=timezone.now)
    favs = models.ManyToManyField('favorites.FavoritesModel', blank=True)
    genre = models.CharField(choices=CHOICES, default=GENERAL, max_length=3)
    discussion = models.ManyToManyField(DiscussionModel, null=True, blank=True)
    comments = models.ManyToManyField(CommentModel, null=True, blank=True)
    # Add sources.
    
    def __str__(self):
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('home')
