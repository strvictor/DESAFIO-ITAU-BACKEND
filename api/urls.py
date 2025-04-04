
from django.urls import path
from api import views

urlpatterns = [
    path('transacao/', views.TransacaoView.as_view(), name='transacao'),
    path('estatistica/', views.EstatisticaView.as_view(), name='estatistica'),
]
