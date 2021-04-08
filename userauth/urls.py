from django.urls import path
from userauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/update-password.html')),
]
