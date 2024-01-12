from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_username', 'tel']

    def get_username(self, obj):
        return obj.user.username

admin.site.register(Profile, ProfileAdmin)