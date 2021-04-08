from django.db import models
from userauth.models import CustomUser
# Create your models here.

# TODO: Add a body
# TODO: Probably a thread feature.

class DiscussionModel(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.CharField(max_length=300, blank=True)
    # Like
    # thread

    def __str__(self):
        return self.title
    