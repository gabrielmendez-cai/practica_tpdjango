from django.shortcuts import render


# Create your views here.
def home (request):
    return render(request, "core/index.html")

def nosotros (request):
    return render(request, "core/nosotros.html")