from django.db import models
from userauth.models import CustomUser
from django.utils import timezone

# Create your models here.

# TODO: Add a body
# TODO: Probably a thread feature.

class DiscussionModel(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey('woolnews_app.PostModel', on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True)
    favs = models.ManyToManyField('favorites.FavoritesModel', blank=True, null=True)
    # To avoid circular imports we call the model with a string.
    comments = models.ManyToManyField('woolnews_app.CommentModel', blank=True,null=True)
    timestamp = models.TimeField(default=timezone.now)
    # True for Active, false for closed.
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    