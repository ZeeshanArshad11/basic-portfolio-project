from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog(request):
    allblog = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blogs':allblog})
