from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Post
# Create your views here.

def Base(request): #request = requisição
    return render(request, 'paginas/home.html')#render sempre recebe primeiro o request depois o template

def About(request):
    return render(request, 'paginas/about.html')

def Portifolio(request):
    return render(request, 'paginas/portifolio.html')

def Page(request):
    search = request.GET.get('search')

    if search:
        posts = Post.objects.filter(title__icontains=search) 
    else:
        posts_list = Post.objects.all().order_by('-created_at') #mostar os posts
        paginator = Paginator(posts_list,len(posts_list)) #Dê ao Paginator uma lista de objetos, mais o número de itens que você gostaria de ter em cada página, e ele fornece métodos para acessar os itens de cada página
        page = request.GET.get('page') #tentando alcançar aqui é encontrar o valor para a chave 'página' fornecida
        posts = paginator.get_page(page) # "refresh" na pagina com o resultado da busca

    return render(request, 'paginas/index.html', {'posts': posts})


def Postview(request, id):
    post = get_object_or_404(Post, pk=id)#recebe o model e o id
    return render(request,'paginas/post.html', {'post': post})

