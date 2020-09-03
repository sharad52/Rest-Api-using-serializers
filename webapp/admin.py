from django.contrib import admin
from .models import userInfo

# Register your models here.
@admin.register(userInfo)
class userAdmin(admin.ModelAdmin):
    pass