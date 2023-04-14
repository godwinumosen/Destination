from django.contrib import admin
from . import models

from .models import ProductDestination


class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title','price','offer','slug','option']
    
admin.site.register(models.ProductDestination,AuthorAdmin)