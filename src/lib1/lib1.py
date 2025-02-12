import requests

def funcao_lib1(nome):
    resposta = requests.get(f'https://api.agify.io?name={nome}')
    idade = resposta.json().get('age')
    return f'Olá da lib1, {nome}! Sua idade estimada é {idade}.'
