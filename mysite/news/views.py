from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.all()
    Categories = Category.objects.all()

    context = {
        'news': news,
        'title': 'Список новостей',
        'Categories': Categories
    }
    return render(request,  template_name='news/index.html', context=context)


def get_category(request, Category_id):
    news = News.objects.filter(Category_id=Category_id)
    Categories = Category.objects.all()
    category = Category.objects.get(pk=Category_id)
    return render(request, 'news/Category.html', {'news': news, 'Categories': Categories, 'category': category})
