from django.urls import path
from . import views

app_name = 'app_proposta'

urlpatterns = [
    path('solicitar_proposta/', views.solicitar_proposta, name='solicitar_proposta'),
    path('mensagem_sucesso/', views.mensagem_sucesso, name='mensagem_sucesso'),
]
