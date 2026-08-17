from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_request),
    path('post/', views.post_request)
]