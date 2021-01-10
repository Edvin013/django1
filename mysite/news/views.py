from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('helo')


def test(request):
    return HttpResponse('<h1>test stranica</h1>')    
