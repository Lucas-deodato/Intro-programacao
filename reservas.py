import json
import os
from datetime import datetime

arquivo = os.path.join(os.path.dirname(__file__), "reservas.json")


# Função auxiliar para verificar conflitos
def verifica_conflitos(reservas, nova_reserva):
    """
    Verifica se uma nova reserva possui conflitos com reservas existentes.

    Parameters:
    - reservas (list): Uma lista de dicionários representando reservas existentes.
    - nova_reserva (dict): Um dicionário representando a nova reserva a ser verificada.

    Returns:
    - bool: Retorna True se houver conflito(s), indicando que a nova reserva não pode ser feita.
            Retorna False caso contrário, indicando que a nova reserva é válida.
    """

    for reserva_existente in reservas:
        conflito = (
            (
                nova_reserva.get("nome_restaurante")
                == reserva_existente.get("nome_restaurante")
            )
            and (nova_reserva.get("horario") == reserva_existente.get("horario"))
            and (
                nova_reserva.get("qtd_pessoas") == reserva_existente.get("qtd_pessoas")
            )
        )

        if conflito:
            return True
    return False


# CREATE: CRIAR RESERVA
def reservar(nome_restaurante, nome, cpf, data, qtd_pessoas, horario, mesa):
    """
    Reserva um lugar no restaurante especificado para o número de pessoas indicado,
    no dia e horário solicitado.

    Parameters:
    - nome_restaurante (str): Nome do restaurante onde a reserva será feita.
    - nome (str): Nome do cliente fazendo a reserva.
    - cpf (str): CPF do cliente fazendo a reserva.
    - data (str): Data desejada para a reserva (dd/mm/yyyy).
    - qtd_pessoas (int): Quantidade de pessoas para a reserva.
    - horario (str): Horário desejado para a reserva (HH:MM).
    - mesa (int): Número da mesa preferencial para a reserva.

    Returns:
    None
    """

    try:
        with open(arquivo, "r", encoding="utf8") as f:
            reservas = json.load(f)

        nova_reserva = {
            "nome_restaurante": nome_restaurante,
            "nome": nome,
            "cpf": cpf,
            "data": data,
            "qtd_pessoas": qtd_pessoas,
            "horario": horario,
            "mesa": mesa,
        }

        # Verifica conflitos antes de adicionar a nova reserva
        if verifica_conflitos(reservas, nova_reserva):
            print(
                "Não foi possível criar a reserva. Horário, número de pessoas e restaurante já estão ocupados."
            )
        else:
            reservas.append(nova_reserva)
            with open(arquivo, "w", encoding="utf8") as f:
                json.dump(reservas, f, indent=4)
            print(
                "😎 RESERVA CONFIRMADA! \n"
                f"Restaurante: {nome_restaurante}\nData: {data}\nHorário: {horario}\nMesa: {mesa}\nPessoas: {qtd_pessoas} "
            )
    except FileNotFoundError:
        print(
            "Arquivo não encontrado. Por favor, crie o arquivo 'reservas.json' primeiro."
        )


# READ: LER TODAS AS RESERVAS
def listar_reservas():
    """
    Lista todas as reservas existentes do arquivo 'reservas.json'.

    Esta função lê o arquivo 'reservas.json' e imprime os detalhes de cada reserva,
    incluindo o nome do restaurante, a data, a hora e o número da tabela.

    Se não houver reservas, ele informará ao usuário que todos os horários estão disponíveis.
    """

    with open(arquivo, "r", encoding="utf8") as f:
        reservas = json.load(f)

    if reservas:
        print("=" * 50)
        print("RESERVAS:")
        print("-" * 50)
        for r in reservas:
            print("*" * 35)
            print(
                f"Restaurante: {r['nome_restaurante']}\nHorário: {r['horario']}\nMesa: {r['mesa']}"
            )
            print("*" * 35)
    else:
        print("NENHUMA RESERVA EFETUADA AINDA, TODOS OS HORÁRIOS ESTÃO DISPONÍVEIS.")


# UPDATE: ATUALIZAR O HORÁRIO DA RESERVA
def atualizar_reserva(cpf, nova_data, novo_horario):
    """
    Atualiza a data e a hora de uma reserva feita por um cliente identificado pelo seu CPF.

    Parameters:
    - cpf (str): o CPF do cliente usado para identificar a reserva.
    - nova_data (str): a nova data para a reserva no formato dd/mm/yyyy
    - novo_horario (str): o novo horário para a reserva no formato hh:mm.

    Returns:
    None
    """

    with open(arquivo, "r", encoding="utf8") as f:
        reservas = json.load(f)

    for r in reservas:
        if r["cpf"] == cpf:
            r["horario"] = novo_horario
            r["data"] = nova_data

            with open(arquivo, "w", encoding="utf8") as f:
                json.dump(reservas, f, indent=4)

            print("😙 HORÁRIO DA RESERVA ATUALIZADO COM SUCESSO!!")
            break
        else:
            print("O CPF não consta na lista de reservas.")


# DELETE: CANCELAR A RESERVA
def cancelar_reserva(cpf):
    """
    Cancela uma reserva associada ao cpf informado.

    Parameters:
    - cpf (str): o CPF do usuario que consta na reserva que deseja-se cancelar.

    Returns:
    None
    """

    with open(arquivo, "r", encoding="utf8") as f:
        reservas = json.load(f)

    for r in reservas:
        if r["cpf"] == cpf:
            reservas.remove(r)

            with open(arquivo, "w", encoding="utf8") as f:
                json.dump(reservas, f, indent=4)

            print("😡 RESERVA CANCELADA COM SUCESSO!")
            break
        else:
            print("O CPF não consta na lista de reservas.")


# VERIFICAR APENAS A SUA RESERVA
def verificar_reserva(cpf):
    """
    Verifica e exibe apenas as reservas feitas pelo CPF fornecido.

    Parameters:
    - cpf (str): O CPF do usuário titular das reservas que deseja-se verificar

    Returns:
        None
    """

    with open(arquivo, "r", encoding="utf8") as f:
        reservas = json.load(f)
        reservas_filtradas = [r for r in reservas if r["cpf"] == cpf]

        if reservas_filtradas:
            for r in reservas_filtradas:
                print("--- Dados da reserva ---\n")
                print(
                    f"Nome: {r['nome']}\nCPF: {r['cpf']}\nData: {r['data']}\nN° de pessoas: {r['qtd_pessoas']}\nHorário: {r['horario']}\nMesa: {r['mesa']}"
                )
        else:
            print("Reserva não encontrada.")


def reservas_proximas():
    """
    Recupera e retorna a lista de reservas agendadas para hoje ou mais tarde.

    Esta função filtra as reservas existentes com base na data e hora atuais,
    retornando apenas aqueles que estão agendados para datas de hoje ou futuras.

    Returns:
        list: Uma lista de dicionários que representam as reservas filtradas.
    """

    with open(arquivo, "r", encoding="utf8") as f:
        reservas = json.load(f)
        hoje = datetime.now().date()
        hora_atual = datetime.now().time()

        reservas_filtradas = []
        for reserva in reservas:
            reserva_data = datetime.strptime(reserva["data"], "%d/%m/%Y").date()
            reserva_horario = datetime.strptime(reserva["horario"], "%H:%M").time()

            if reserva_data >= hoje and (
                reserva_horario.hour >= hora_atual.hour
                and reserva_horario.minute >= hora_atual.minute
            ):
                reservas_filtradas.append(reserva)

        return reservas_filtradas
