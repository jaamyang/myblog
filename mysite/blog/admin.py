from django.contrib import admin
from .models import Cate,Blog

# Register your models here.

@admin.register(Cate)
class CateAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','blog_type','author','is_delete','created_time','last_updated')
    search_fields = ['title']
    