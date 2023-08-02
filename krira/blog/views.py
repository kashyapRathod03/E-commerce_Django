from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    # return HttpResponse("index blog")
    return render(req,'blog/index.html')