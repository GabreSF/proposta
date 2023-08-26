from celery import shared_task
from .models import Proposta

@shared_task
def processar_proposta(proposta_id):
    try:
        proposta = Proposta.objects.get(id=proposta_id)
        
        if len(proposta.descricao) > 100:
            proposta.aprovada = True
            proposta.save()
        else:
            proposta.aprovada = False
            proposta.save()
        
        return f"Proposta {proposta_id} processada com sucesso"
    except Proposta.DoesNotExist:
        return f"Proposta {proposta_id} não encontrada"
