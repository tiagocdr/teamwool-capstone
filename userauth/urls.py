from django.urls import path
from userauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/update-password.html')),
]
