from django.http import HttpResponse
from .models import Product, Category
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout


def main(request, *args, **kwargs):
    return render(request, 'app_food/base.html')


def catalog(request, *args, **kwargs):
    categories = Category.objects.all()
    return render(request, 'app_food/index.html', context={'categories': categories})


def category(request, *args, **kwargs):
    products = Product.objects.filter(category__id=kwargs['pk'])
    return render(request, 'app_food/category.html', context={
        'products': products
    })












def main_page(request, *args, **kwargs):
    return render(request, 'app_food/base.html')


def login_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'app_food/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main')

    return render(request, 'app_food/login.html', {'error': 'auth error'})

class MyLogoutView(LogoutView):
    next_page = reverse_lazy('main')


def logout_view(request):
    logout(request)
    return redirect('main')