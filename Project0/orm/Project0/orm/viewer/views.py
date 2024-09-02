from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def hello(request):
#     return HttpResponse('Hello, world!')
def hello(request, s):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} word!')

def hello(request, s0):
  s1 = request.GET.get('s1', '')
  return render(
    request, template_name='hello.html',
    context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
  )