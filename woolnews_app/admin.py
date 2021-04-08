from django.contrib import admin
from .models import PostModel, CommentModel # GenreModel
from userauth.models import CustomUser


admin.site.register(PostModel)
admin.site.register(CommentModel)

# admin.site.register(GenreModel)