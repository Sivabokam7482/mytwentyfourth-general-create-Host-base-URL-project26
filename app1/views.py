from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def siva(request):
    return HttpResponse('<h1><i>THIS IS BASE URL TO IP ADDRESS</i></h1>')
