from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import *
from app.models import Tumanlar


class IndexView(ListView):
    model = Shaharlar
    template_name = 'index.html'


class ThreePage(ListView):
    model = Loyiha_turlari
    loyiha = Loyiha_turlari.objects.all()
    template_name = 'loyiha/uchtalikpage.html'
    extra_context = {
        'loyha': loyiha
    }


# class TwoPage(ListView):
#     model = Holati
#     holati = Holati.objects.all()
#     template_name = 'loyiha/sanoat_ikkitalikpage/ikkitalipage.html'
#     extra_context = {
#         'holati': holati
#     }


# class Tugallangan(ListView):
#     model = Loyihalar
#     loyihalar = Loyihalar.objects.all()
#     holati = Holati.objects.all()
#     template_name = 'loyiha/tugallangan.html'
#     extra_context = {
#         'loyihalar': loyihalar,
#         'holati': holati
#     }


def contact(request):
    if request.method == 'POST':
        print('added')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        text = request.POST.get("text")

        c = Contact()
        c.first_name = first_name
        c.last_name = last_name
        c.email = email
        c.phone_number = phone_number
        c.text = text

        c.save()

    return render(request, 'contact.html')


def sanoat_2(request):
    return render(request, 'loyiha/ikkitalikpage/sanoat.html')


def qishloq_2(request):
    return render(request, 'loyiha/ikkitalikpage/qishloq.html')


def xizmat_2(request):
    return render(request, 'loyiha/ikkitalikpage/xizmat.html')


class SanoatTick(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallangan/sanoat.html'


class QishloqTick(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallangan/qishloq.html'


class XizmatTick(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallangan/xizmat.html'


class SanoatX(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallanmagan/sanoat.html'


class QishloqX(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallanmagan/qishloq.html'


class XizmatX(ListView):
    model = Loyihalar
    loyiha = Loyihalar.objects.all()
    template_name = 'loyiha/tugallanmagan/xizmat.html'


class LoyihaSingle(DetailView):
    model = Loyihalar
    template_name = 'loyiha/single.html'


class TumanlarView(ListView):
    model = Tumanlar
    template_name = 'tuman/tuman.html'


class TumanSingle(DetailView):
    model = Tumanlar
    template_name = 'tuman/single.html'

