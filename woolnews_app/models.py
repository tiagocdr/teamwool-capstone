from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from userauth.models import CustomUser
<<<<<<< HEAD

# TODO : Favorite Model.
# TODO : Image Implementation.
# TODO : Genres, probably a foreign key to posts
# TODO : Forum, a model with a post and user foreign key, this would be where the discussion part would.
# TODO : Favorites, still thinking about how to best implement it

# class CustomUser(AbstractUser):
#     pass

#     # add additional fields in here

#     def __str__(self):
#         return self.username
=======
from django.urls import reverse
# TODO: Automatically default to a general genre if not provided one.


class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    timestamp = models.TimeField(default=timezone.now)
    votes = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.text} | {self.user}'


# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     img = models.ImageField(upload_to='images/', blank=True)
    
#     def __str__(self):
#         return str(self.user)
>>>>>>> 276745b13cda10a698ad404ad62dd2c9c7e8b13a


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
<<<<<<< HEAD
    support = models.IntegerField(default=0, blank=True)
    # comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)
=======
    favs = models.ManyToManyField('favorites.FavoritesModel', blank=True)
    genre = models.CharField(choices=CHOICES, default=GENERAL, max_length=3)
    discussion = models.ManyToManyField(DiscussionModel, null=True, blank=True)
    comments = models.ManyToManyField(CommentModel, null=True, blank=True)
    likes = models.ManyToManyField(CustomUser, related_name='blog_posts')
>>>>>>> 276745b13cda10a698ad404ad62dd2c9c7e8b13a

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
<<<<<<< HEAD
        return self.title


class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    timestamp = models.TimeField(default=timezone.now)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} | {self.user}'
=======
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('home')
>>>>>>> 276745b13cda10a698ad404ad62dd2c9c7e8b13a
