from django.urls import path
from .views import main, catalog, category
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .views import main_page, login_view, logout_view, MyLogoutView

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('', main, name='main'),
    path('catalog/category/<int:pk>/', category, name='category'),
    path('login/', LoginView.as_view(template_name='app_food/login.html', redirect_authenticated_user=True), name='login'),
    path('logout', MyLogoutView.as_view(), name='logout')
]

