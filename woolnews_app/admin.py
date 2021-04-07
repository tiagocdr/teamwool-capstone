from django.contrib import admin
from .models import PostModel, CommentModel



admin.site.register(PostModel)
admin.site.register(CommentModel)
