from django.shortcuts import render
from django.views.generic import ListView

from app.models import Shaharlar, Tumanlar, Loyihalar


class IndexView(ListView):
    model = Shaharlar
    shaharlar = Shaharlar.objects.all()
    tumanlar = Tumanlar.objects.all()
    loyihalar = Loyihalar.objects.all()
    template_name = 'index.html'
    extra_context = {
        'shaharlar': shaharlar,
        'tumanlar': tumanlar,
        'loyihalar': loyihalar,
    }


def about(request):
    return render(request, 'about.html')


def books(request):
    return render(request, 'books.html')


def contact(request):
    return render(request, 'contact.html')


def work_with_me(request):
    return render(request, 'loyihalar.html')


def single(request):
    return render(request, 'single.html')

