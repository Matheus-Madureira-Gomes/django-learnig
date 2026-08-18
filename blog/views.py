from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_request(request):
    return render(request, 'blog/blog.html')

def post_request(request):
    return HttpResponse('Posts do blog!')