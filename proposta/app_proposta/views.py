import requests
from django.shortcuts import render, redirect
from .forms import SolicitacaoPropostaForm
from .models import Proposta

def mensagem_sucesso(request):
    return render(request, 'mensagem_sucesso.html')

def solicitar_proposta(request):
    if request.method == 'POST':
        form = SolicitacaoPropostaForm(request.POST)
        if form.is_valid():
            nova_proposta = Proposta(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                descricao=form.cleaned_data['descricao']
            )
            nova_proposta.save()
            
            payload = {
                "document": nova_proposta.document,
                "name": nova_proposta.nome
            }
            
            api_url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
            response = requests.post(api_url, json=payload)
            
            if response.status_code == 200:
                loan_response = response.json()
                if loan_response.get('approved', False):
                    nova_proposta.aprovada = True
                    nova_proposta.save()
                    return redirect('app_proposta:mensagem_sucesso')
                else:
                    return render(request, 'mensagem_reprovada.html')  
            else:
                return render(request, 'erro_api.html', {'erro': 'Erro na API'})
    else:
        form = SolicitacaoPropostaForm()
    
    return render(request, 'solicitar_proposta.html', {'form': form})
