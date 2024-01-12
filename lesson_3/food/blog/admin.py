from django.contrib import admin
from .models import Author, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published_at', 'update_at', 'status_choices']
    # list_filter = ['authors']
    search_fields = ['first_name', 'last_name']


admin.site.register(News, NewsAdmin)
admin.site.register(Author)