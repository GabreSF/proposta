from django.contrib import admin
from .models import Proposta


def aprovar_propostas(modeladmin, request, queryset):
    queryset.update(aprovada=True)

aprovar_propostas.short_description = "Aprovar propostas selecionadas"

def negar_propostas(modeladmin, request, queryset):
    queryset.update(aprovada=False)

negar_propostas.short_description = "Negar propostas selecionadas"


@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'descricao', 'aprovada')
    list_filter = ('aprovada',)
    actions = [aprovar_propostas, negar_propostas]
