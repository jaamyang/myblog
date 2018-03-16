from django.shortcuts import render_to_response
from blog import models

def home(request):
    context = {}
    context["home"] = models.Blog.objects.filter(is_delete = False).order_by('-created_time')[:2]
    context["blog_type"] = models.Cate.objects.all()
    return render_to_response('home.html',context)