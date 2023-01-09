from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample1(request):
    return HttpResponse('<h1>hello Madhu DG</h1>')

def sample2(request):
    return HttpResponse('<marquee>How Are You</marquee>')