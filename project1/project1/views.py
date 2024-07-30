from django.http import HttpResponse


def Home(request):
    return HttpResponse("hello my name is saurabh")

def Blog(request):
    return HttpResponse("hello this part  is from  blog")

