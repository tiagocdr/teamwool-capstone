from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
<<<<<<< HEAD

=======
    bio = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='images/', blank=True)
    # Image.
>>>>>>> 276745b13cda10a698ad404ad62dd2c9c7e8b13a
    # favorites = models.ManyToManyField(PostModel, on_delete=models.CASCADE, blank=True)
    # add additional fields in here
    def __str__(self):
        return self.username
<<<<<<< HEAD


=======
    pass
>>>>>>> 276745b13cda10a698ad404ad62dd2c9c7e8b13a
