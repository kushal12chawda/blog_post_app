from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category, Post

# Create your views here.


def home(request):
    post = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts': post,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    return render(request, 'category.html', {'cat':cat, 'post':post})
