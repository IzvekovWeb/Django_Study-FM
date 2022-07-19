from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context)


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас'})


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Пост {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по категориям',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)



# def categories(request, cat_id):
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f"<h1>Страница categories {cat_id}</h1>")
#
#
# def archive(request, year):
#     if int(year) > 2021:
#         raise Http404()
#     elif int(year) < 2000:
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>Архив данных {year}</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
