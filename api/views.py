__author__ = 'Tim Garner'
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('Tim Garner SOFT338 API - '
                        'if you are looking for documentation please visit <a href="/docs/">docs')