from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Cesare De Cal',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 1st, 2020'
    },
    {
        'author': 'Giulia Marcella',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 2nd, 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
