
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import  UserChangeForm

# SignUp View
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(CreateView):
    form_class = UserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'