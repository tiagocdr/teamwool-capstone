from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, PostModel, CommentModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(PostModel)
admin.site.register(CommentModel)
