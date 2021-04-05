from django.urls import path
from woolnews_app import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup')
]
