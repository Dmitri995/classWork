import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def news_list(request, *args, **kwargs):
    data = {
        'date_now': datetime.datetime.now(),
        # 'news_categories': ('Criminal', 'Politics', 'Sport')
    }
    return render(request, 'app_news/index.html', context=data)