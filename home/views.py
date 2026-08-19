from django.shortcuts import render
from home.data import posts

# Create your views here.

context = {
    'posts': posts
}

def home_request(request):
    return render(request, 'home/home.html', context)