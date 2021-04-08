
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, EditProfileForm
from django.contrib.auth.forms import  UserChangeForm

# SignUp View
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('home')
    template_name = 'edit_profile.html'
    
    def get_object(self):
        return self.request.user