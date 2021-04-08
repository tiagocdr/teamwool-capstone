
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import CreateView
from django.views import View

from .models import CustomUser
from .forms import CustomUserCreationForm

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

    def get(self, request):
        template_name = "registration/signup.html"
        form = CustomUserCreationForm()
        return render(request, template_name, {"form": form, "header": "Signup"})
