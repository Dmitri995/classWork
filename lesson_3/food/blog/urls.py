from django.urls import path
from .views import NewsListView, RegiterNews


# class RegiterNews:
#     pass


urlpatterns = [
    path('news-list/', NewsListView.as_view(), name='news-list'),
    path('new_news/', RegiterNews.as_view(), name='register-news')

]