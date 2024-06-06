"""
This module manages restaurant reservations, 
    including creating, reading, updating, and deleting reservations.
    It interacts with a JSON file named 'reservas.json' to store reservation data.
"""

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
        # Use.get() para acessar valores de dicionário e
        # fornecer um valor padrão caso a chave não exista
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
    Lists all existing reservations from the 'reservas.json' file.

    This function reads the 'reservas.json' file and prints out each reservation's details,
    including the restaurant name, date, time, and table number.

    If there are no reservations, it informs the user that all timeslots are available.
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
    Updates the date and time of a reservation made by a customer identified by their CPF.

    Parameters:
    - cpf (str): The customer's CPF used to identify the reservation.
    - nova_data (str): The new date for the reservation in the format dd/mm/yyyy.
    - novo_horario (str): The new time for the reservation in the format HH:MM.

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
    Cancels a reservation associated with the given CPF.

    Parameters:
    - cpf (str): The CPF of the reservation holder whose reservation is to be canceled.

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
    Verifies and displays only the reservations made by the given CPF.

    Parameters:
    - cpf (str): The CPF of the reservation holder whose reservations are to be verified.

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
    Retrieves and returns the list of reservations scheduled for today or later.

    This function filters the existing reservations based on the current date and time,
    returning only those that are scheduled for today or future dates.

    Returns:
        list: A list of dictionaries representing the filtered reservations.
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
