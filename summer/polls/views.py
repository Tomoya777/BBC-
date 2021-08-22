from django.shortcuts import render
from .models import Blog

<<<<<<< HEAD
def index_templates(request):
    return render(request, 'index.html')

def index_templates1(request):
    return render(request, 'active.html')
=======
def toppage(request):
    return render(request, 'toppage.html')
    
def blog(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blog.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'detail.html', {'blog': blog})
>>>>>>> 0db77fd43ee90b34e8cd887f87732e8e2571d67a
