from django.urls import path
from app.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('threepage/', ThreePage.as_view(), name='threepage'),
    # path('twopage/', TwoPage.as_view(), name='twopage'),
    path('contact/', contact, name='contact'),
    path('tumanlar/', TumanlarView.as_view(), name='tuman'),
    # path('tugallangan/', Tugallangan.as_view(), name='tugallangan'),
    path('sanoat_2/', sanoat_2, name='sanoat_2'),
    path('qishloq_2/', qishloq_2, name='qishloq_2'),
    path('xizmat_2/', xizmat_2, name='xizmat_2'),
    path('sanoat_tick/', SanoatTick.as_view(), name='sanoat_tick'),
    path('qishloq_tick/', QishloqTick.as_view(), name='qishloq_tick'),
    path('xizmat_tick/', XizmatTick.as_view(), name='xizmat_tick'),
    path('sanoat_x/', SanoatX.as_view(), name='sanoat_x'),
    path('qishloq_x/', QishloqX.as_view(), name='qishloq_x'),
    path('xizmat_x/', XizmatX.as_view(), name='xizmat_x'),
    path('loyiha_single/<int:pk>/', LoyihaSingle.as_view(), name='loyiha_single'),
    path('tuman_single/<int:pk>/', TumanSingle.as_view(), name='tuman_single'),
    # path('tugallangan/', Tugallangan.as_view(), name='tugallangan'),
    # path('loyiha/', LoyihaView.as_view(), name='work_with_me'),
    # path('details/<int:pk>/', SinglePage.as_view(), name='details'),

]


