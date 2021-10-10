
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def welcome(req):
    #return HttpResponse('hi')
    return render(req,'welcome.html')


# Create your views here.
