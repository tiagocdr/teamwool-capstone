from django.contrib import admin
from .models import PostModel, CommentModel, GenreModel, Profile



admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(GenreModel)
admin.site.register(Profile)