from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def good_bye(request, *args, **kwargs):
    return HttpResponse(f'Good Bye!')
