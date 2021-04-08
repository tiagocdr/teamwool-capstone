from django.urls import path
from userauth import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile')
]
