from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Subhas. You're at the polls index.")

def indexhere(request):
    return HttpResponse("Yeh ladki pagal he pagal he pagal he :-) ******************")