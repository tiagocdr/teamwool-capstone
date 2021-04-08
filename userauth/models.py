from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    # Image.
    # favorites = models.ManyToManyField(PostModel, on_delete=models.CASCADE, blank=True)
    # add additional fields in here
    def __str__(self):
        return self.username
    pass
