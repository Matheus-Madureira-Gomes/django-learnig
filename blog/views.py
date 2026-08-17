from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog_request(request):
    return HttpResponse('Blog app')

def post_request(request):
    return HttpResponse('Posts do blog!')