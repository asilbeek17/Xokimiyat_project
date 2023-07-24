from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


def contact(request):
    return render(request, 'contact.html')


class LoyihaView(ListView):
    model = Loyihalar
    loyihalar = Loyihalar.objects.all()
    template_name = 'loyihalar.html'

    extra_context = {
        'loyihalar': loyihalar
    }


class SinglePage(DetailView):
    model = Loyihalar
    template_name = 'single.html'
