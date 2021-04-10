from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from discussion.models import DiscussionModel
from userauth.models import CustomUser

# TODO: Automatically default to a general genre if not provided one.

class GenreModel(models.Model):
    CHOICES = (
        ('At','Automotive'),
        ('Sp', 'Sports'),
        ('At','Arts'),
        ('Pl','Politics'),
        ('CC','Climate Change'),
        ('Op','Opinion'),
        ('DJ','DadJokes'),
        ('def', 'general')
    )
    name = models.CharField(choices=CHOICES, max_length=20, default='def')

    def __str__(self):
        return self.name

class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    timestamp = models.TimeField(default=timezone.now)
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.text} | {self.user}'


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.TimeField(default=timezone.now)
    support = models.IntegerField(default=0, blank=True)
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE,  null=True)
    discussion = models.ManyToManyField(DiscussionModel, null=True, blank=True)
    comments = models.ManyToManyField(CommentModel, null=True, blank=True)

    def __str__(self):
        return self.title



