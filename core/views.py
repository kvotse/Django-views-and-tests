from django.shortcuts import render, get_object_or_404
from django.views import View
from . import models
from django.views.generic import RedirectView, FormView
from .form import SimpleForm


class IndexView(View):
    def get(self, request):
        news = models.News.objects.all()
        categories = models.Category.objects.all()
        context = {
            'news': news,
            'categories': categories,
            'title': 'Список новостей',
        }
        return render(request, 'core/index.html', context=context)


class CategoryView(View):
    def get(self, request, category_id):
        news = models.News.objects.filter(category=category_id)
        categories = models.Category.objects.all()
        category = get_object_or_404(models.Category, pk=category_id)
        context = {
            'news': news,
            'categories': categories,
            'category': category,
        }
        return render(request, 'core/category.html', context=context)


class RedirectView(RedirectView):
    url = 'https://github.com/dashboard'
    query_string = True


class SimpleForm(FormView):
    template_name = 'core/form.html'
    form_class = SimpleForm
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super ().form_valid(form)
