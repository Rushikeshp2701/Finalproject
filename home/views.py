from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requet):
    return HttpResponse("This is home page ")
