from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def website2(request):
    return render(request,'admin1/index.html')