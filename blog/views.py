from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(requests):
    return HttpResponse("Hey there. ")
def post(requests):
    return HttpResponse("I;m a single post page.")

