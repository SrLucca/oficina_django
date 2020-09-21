from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
# Create your views here.

def Base(request):
    return render(request, 'paginas/home.html')#render sempre recebe primeiro o request depois o template

def About(request):
    return render(request, 'paginas/about.html')

def Page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'paginas/index.html', {'posts': posts})

def Postview(request, id):
    post = get_object_or_404(Post, pk=id)#recebe o model e o id
    return render(request,'paginas/post.html', {'post': post})

