from discussion.models import DiscussionModel
from django.db import models
from userauth.models import CustomUser
from woolnews_app.models import PostModel
from discussion.models import DiscussionModel
# Create your models here.

class FavoritesModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, blank=True, null=True)
    discussion = models.ForeignKey(DiscussionModel, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'forum ' + str(self.discussion) + '|' + 'post '+ str(self.post) + ' | ' + str(self.user)

    def get_fav_count(self):
        return self.user.count()