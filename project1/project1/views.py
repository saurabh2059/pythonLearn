from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return HttpResponse("hello my name is saurabh")

def Blog(request):
    return HttpResponse("hello this part  is from  blog")


def BlogPage(request):
 return render(request, "index.html")