from django.shortcuts import render
from django.http import HttpResponse
def django_fees(request):
    return HttpResponse('<h1>1000</h1>')
def python_fees(request):
    return HttpResponse('<h1>2000</h1>')