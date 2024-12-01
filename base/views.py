from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requests):
    return HttpResponse('<h2>Home</h2>')

def posts(requests):
    return HttpResponse('<h2>Posts</h2>')

def post(requests):
    return HttpResponse('<h2>Post title</h2>')

def profile(requests):
    return HttpResponse('<h2>User profile</h2>')