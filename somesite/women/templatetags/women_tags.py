from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/tags_templates/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not filter:
        cats = Category.objects.all()
    else:
        cats = Category.objects.all().order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/tags_templates/top_menu.html')
def show_top_menu():
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статьи', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
    ]
    return {'menu': menu}
