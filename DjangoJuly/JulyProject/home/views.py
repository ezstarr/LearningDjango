from django.shortcuts import render, HttpResponse

# HttpResponse is a class, whose output is a view.

# Create your views here.
def home(request):
    return HttpResponse("This is the data")

def path(request):
    return HttpResponse("This a path view, of esther")