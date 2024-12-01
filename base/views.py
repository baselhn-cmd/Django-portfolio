from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse(requests, 'base/index.html')

def posts(requests):
    return HttpResponse(requests, 'base/posts.html')

def post(requests):
    return HttpResponse(requests, 'base/post.html')

def profile(requests):
    return HttpResponse(requests, 'base/profile.html')