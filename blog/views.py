from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(requests):
    posts = Post.objects.all()
    return render(requests, 'index.html', {'posts': posts   })


def post(requests):
    return HttpResponse("I'm a single post page.")

