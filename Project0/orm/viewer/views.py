from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def hello(request):
#     return HttpResponse('Hello, world!')
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} word!')
