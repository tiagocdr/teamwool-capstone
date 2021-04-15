from django.shortcuts import render

# Create your views here.


def automotive_view(request):
    return render(request, 'genres.html')


def arts_view(request):
    return render(request, 'genres.html')


def cc_view(request):
    return render(request, 'genres.html')


def dadjokes_view(request):
    return render(request, 'genres.html')
    

def opinion_view(request):
    return render(request, 'genres.html')



def politics_view(request):
    return render(request, 'genres.html')
