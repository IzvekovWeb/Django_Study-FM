from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *


# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#     return render(request, 'women/index.html', context)

class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    # extra_context = {'title': 'Главная страница'}  # только статические данные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        # context['menu'] = menu  # так можно передавать динамические данные. У меня передается через tags_templates
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


def about(request):
    return render(request, 'women/about.html', {'title': 'О нас'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление статьи"
        return context


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Women.objects.create(**form.cleaned_data)  #форма НЕ связана с моделью
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#     return render(request, 'women/post.html', context=context)


# Вариант 2: класс представления
class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория - " + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# Вариант 1: функция представления
# def show_category(request, cat_slug):
#     posts = Women.objects.filter(cat_id__slug=cat_slug)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'Отображение по категориям',
#         'cat_selected': cat_slug
#     }
#     return render(request, 'women/index.html', context=context)

# Вариант 0
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
