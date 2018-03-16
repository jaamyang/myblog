from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,Cate

# Create your views here.
def blog_list(request):
    context = {}
    current_page = request.GET.get("page",1)
    blogs = Blog.objects.filter(is_delete = False).order_by('-created_time')
    pages = Paginator(blogs,5)
    blogs = pages.page(current_page)
    context['blogs'] = blogs
    context['blogs_count'] = Blog.objects.all().count()
    context['pages'] = pages
    context['blog_type'] = Cate.objects.all()
    return render_to_response('blog_list.html',context)

def blog_detail(request,blog_pk):
    blog = get_object_or_404(Blog,pk = blog_pk) 
    context = {}
    context['pervious_blog'] = Blog.objects.filter(created_time__lt = blog.created_time,is_delete = False).last()
    context['next_blog'] = Blog.objects.filter(created_time__gt = blog.created_time,is_delete = False).first()
    context['blog'] = blog
    return render_to_response('blog_detail.html',context)

def blog_with_type(request,blog_type_pk):
    context = {}
    btype = get_object_or_404(Cate,pk = blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type = btype,is_delete = False)
    context['blog_type'] = btype
    return render_to_response('blog_with_type.html',context)