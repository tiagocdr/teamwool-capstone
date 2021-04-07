from django.db import models
from django.db.models.fields.related import ForeignKey
from userauth.models import CustomUser
from woolnews_app.models import PostModel
# Create your models here.

class FavoritesModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)