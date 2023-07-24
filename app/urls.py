from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('loyiha/', LoyihaView.as_view(), name='work_with_me'),
    path('details/<int:pk>/', SinglePage.as_view(), name='details'),

]
