import json
import os

arquivo = os.path.join(os.path.dirname(__file__), "listagemRestaurantes.json")


def adicionar_restaurante(nome, endereco, informacoes, funcionamento, avaliacao):
    with open(arquivo, "r", encoding="utf8") as f:
        restaurante = json.load(f)

    restaurante.append(
        {
            "nome": nome,
            "endereco": endereco,
            "informacoes": informacoes,
            "funcionamento": funcionamento,
            "avaliacao": avaliacao,
        }
    )

    with open(arquivo, "w", encoding="utf8") as f:
        json.dump(restaurante, f, indent=4)

    print("😎 Restaurante adicionado!")


def listar_restaurantes():
    with open(arquivo, "r", encoding="utf8") as f:
        restaurantes = json.load(f)

    if restaurantes:
        print("=" * 50)
        print("RESTAURANTES:")
        print("-" * 50)
        for r in restaurantes:
            print("*" * 35)
            print(
                f"Nome do restaurante: {r['nome']}\nInformações: {r['informacoes']}\nFuncionamento: {r['funcionamento']}\nAvaliação: {r['avaliacao']}"
            )


def atualizar_restaurantes(
    nome_atual,
    novo_nome,
    novas_informacoes,
    novo_endereco,
    novo_funcionamento,
    nova_avaliacao,
):
    with open(arquivo, "r", encoding="utf8") as f:
        restaurantes = json.load(f)

    for r in restaurantes:
        if r["nome"] == nome_atual:
            r["nome"] = novo_nome
            r["informacoes"] = novas_informacoes
            r["endereco"] = novo_endereco
            r["funcionamento"] = novo_funcionamento
            r["avaliacao"] = nova_avaliacao

            with open(arquivo, "w", encoding="utf8") as f:
                json.dump(restaurantes, f, indent=4)

            print("RESTAURANTE ATUALIZADO COM SUCESSO!")
            break
    else:
        print("Restaurante não encontrado na lista")


def excluir_restaurante(nome):
    with open(arquivo, "r", encoding="utf8") as f:
        restaurantes = json.load(f)

    for r in restaurantes:
        if r["nome"] == nome:
            restaurantes.remove(r)

            with open(arquivo, "w", encoding="utf8") as f:
                json.dump(restaurantes, f, indent=4)

            print("RESTAURANTE REMOVIDO COM SUCESSO")
            break
    else:
        print("Restaurante não encontrado na lista")
