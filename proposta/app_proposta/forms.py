from django import forms

class SolicitacaoPropostaForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    descricao = forms.CharField(label='Descrição', widget=forms.Textarea)