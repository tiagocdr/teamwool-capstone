from django.shortcuts import render


# TODO: Post View

# @login_required
# def create_post_view(request):
#     template_name = "generic_form.html"
#     form = PostForm()

#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             post = Post.objects.create(
#                 body=data.get("body"), creator=request.user)
#             return redirect(reverse("post_detail", args=(post.id,)))

#     return render(request, template_name, {"form": form, "header": "Create a Post"})