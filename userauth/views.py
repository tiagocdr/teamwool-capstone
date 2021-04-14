from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from woolnews_app.models import PostModel
from favorites.models import FavoritesModel
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserChangeForm
from woolnews_app.forms import PostForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render, redirect
from .models import CustomUser
# SignUp View


# def user_profile(request, user_id):
#     user = CustomUser.objects.get(id=user_id)
#     return render(request,'user.html', {'user':user})
    


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    
class ProfileView(TemplateView):
    model = CustomUser
    template_name = 'registration/profile.html'

    def get_queryset(self):
        print(self.kwargs)
        self.User=CustomUser.objects.get(id=self.kwargs["pk"])
        return self.User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_queryset()
        context["user"]= user
        context["own_posts"] = PostModel.objects.filter(user=user)
        context['saved'] = FavoritesModel.objects.filter(user=user)
        return context

    
  
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user
   

