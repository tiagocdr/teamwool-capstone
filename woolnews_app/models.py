from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# TODO: Favorite Model.
# TODO : Image Implementation. 

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    # img = models.ImageField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.TimeField(default=timezone.now)
    support = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    timestamp = models.TimeField(default=timezone.now)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.post, self.user












