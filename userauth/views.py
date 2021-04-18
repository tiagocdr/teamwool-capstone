from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from woolnews_app.models import PostModel
from favorites.models import FavoritesModel
from discussion.models import DiscussionModel
from django.urls import reverse_lazy
from django.views import generic, View
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserChangeForm
from woolnews_app.forms import PostForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import CustomUser
# SignUp View

# TODO ask about reverse lazy..      

# @login_required
# def index_view(request):

#     template_name = "index.html"
#     posts = Post.objects.all().order_by("-created_at")
#     context = {"posts": posts}
#     return render(request, template_name, context)

class SignUpView(View):
    def post(self, request):
        template_name = "registration/signup.html"
        form = CustomUserCreationForm()
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            login(request, user)
            return redirect(reverse("home"))

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
        context["own_forums"] = DiscussionModel.objects.filter(user=user)
        context['saved'] = FavoritesModel.objects.filter(user=user)
        return context

    
  
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'registration/edit_profile.html'
    
    def get_object(self):
        return self.request.user
   

