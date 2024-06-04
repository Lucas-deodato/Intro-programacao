import json
import os
from time import sleep

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo = os.path.join(os.path.dirname(__file__), 'lista-restaurantes.json')


def adicionar_restaurante(nome, info_cozinha, funcionamento, avaliacao):
    with open(arquivo, 'r') as f:
        restaurante = json.load(f)

    restaurante.append({
        "nome": nome,
        "info-cozinha": info_cozinha,
        "funcionamento": funcionamento,
        "avaliacao": avaliacao,
    })

    with open(arquivo, 'w') as f:
        json.dump(restaurante, f, indent=4)

    print("😎 Restaurante adicionado!")


def listar_restaurantes():
    with open(arquivo, 'r') as f:
        restaurantes = json.load(f)

    if restaurantes: 
        print("=" *50)
        print("RESTAURANTES:")
        print("-" *50)

        for r in restaurantes:
            print("*" *35)
            print(f"Nome do restaurante: {r['nome']}\nInformações: {r['informacoes']}\nFuncionamento: {r['funcionamento']}\nAvaliação: {r['avaliacao']}\n")
            print("*" *35)
            print("=" *35)


def atualizar_restaurantes(nome, nome_antigo):
    with open(arquivo, 'r') as f:
        restaurantes = json.load(f)
    
    for r in restaurantes:
        if r['nome'] == nome:
            r['nome'] = nome_antigo

    with open(arquivo, 'w') as f:
        json.dump(restaurantes, f, indent=4)

    print("Nome do restaurante atualizado com sucesso!")


def excluir_restaurante(nome):
    with open(arquivo, 'r') as f:
        restaurantes = json.load(f)
    
    for r in restaurantes:
        if r['nome'] == nome:
            restaurantes.remove(r)

    with open(arquivo, 'w') as f:
        json.dump(restaurantes, f, indent=4)
    
    print("Restaurante removido com sucesso!")