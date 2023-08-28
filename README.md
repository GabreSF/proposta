# Proposta - Sistema de Gerenciamento de Propostas

O projeto Proposta é um sistema de gerenciamento de propostas, onde os usuários podem preencher informações de propostas e obter análises de crédito.

## Instalação

1. Clone este repositório: `git clone https://github.com/GabreSF/proposta.git`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` ou `venv\Scripts\activate` no Windows
4. Instale as dependências: `pip install -r requirements.txt`
5. Configure o banco de dados: `python manage.py migrate`

## Uso

1. Execute o servidor de desenvolvimento: `python manage.py runserver`
2. Acesse o aplicativo em: `http://localhost:8000/solicitar_proposta/`

## Funcionalidades

- Preenchimento de informações de propostas
- Análise de crédito automática
- Aprovação ou reprovação de propostas com base na análise

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m 'Adiciona nova feature'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Crie um novo Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
