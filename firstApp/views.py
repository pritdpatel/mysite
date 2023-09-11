from django.shortcuts import render
# Create your views here.

#class base view and function base view

from django.http import HttpResponse, HttpRequest , HttpResponseRedirect
from django.views import View

# def main_character(request):
#     return HttpResponseRedirect("../../admin")

def main_character(request):
    context = {'username':'prit'}
    return HttpResponse(render(request, "index.html",context))
