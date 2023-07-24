from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
    path('contact/', contact, name='contact'),
    path('work_with_me/', work_with_me, name='work_with_me'),
    path('single/', single, name='single'),
]
