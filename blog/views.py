from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

context = {
    'nome': 'Matheus Madureira'
}

def blog_request(request):
    return render(request, 'blog/blog.html', context)

def post_request(request):
    return HttpResponse('Posts do blog!')