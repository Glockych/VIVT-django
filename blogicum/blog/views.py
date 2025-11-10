from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template_name = 'blog/index.html'
    return HttpResponse(template_name)