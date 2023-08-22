from django.shortcuts import render

# Create your views here.

def fridge_view(request):
    return render(request, "fridge.html")