from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


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

