from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student_1(request):
    return HttpResponse('student 1')
def student_2(request):
    return HttpResponse('student 2')
