from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, I'm from ST5")

def update(request):
    return HttpResponse("Update Content")