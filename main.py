"""
This module provides the main functionality for managing restaurant reservations and listings.
It includes functions for displaying menus, handling user inputs, 
  and interacting with reservation and restaurant data.
"""

import os
from time import sleep
import reservas
import restaurantes

from utils.cor import Cor


arquivo = os.path.join(os.path.dirname(__file__), "reservas.json")


def menu_inicial():
    """
    Displays the initial menu options to the user.

    This function prints the initial menu options available to the user,
    allowing them to select an option to proceed further.
    """

    print(Cor.CIANO + "=" * 55 + Cor.RESET)
    print("          1 - MENU DE RESERVAS")
    print("          2 - MENU DE RESTAURANTES")
    print("          3 - SAIR ")
    print(Cor.CIANO + "=" * 55 + Cor.RESET)


def menu_reservas():
    """
    Displays the reservation menu options to the user.

    This function prints the reservation menu options available to the user,
    allowing them to select an option to proceed further.
    """

    print(Cor.CIANO + "=" * 55 + Cor.RESET)
    print("\n[MENU DE RESERVAS]\n")
    print("1. FAZER RESERVA")
    print("2. LISTAR RESERVAS")
    print("3. ALTERAR DATA/HORA DA RESERVA")
    print("4. CANCELAR RESERVA")
    print("5. VERIFICAR INFORMAÇÕES DA MINHA RESERVA")
    print("6. VOLTAR AO MENU ANTERIOR")
    print(Cor.CIANO + "=" * 55 + Cor.RESET)


def menu_restaurantes():
    """
    Displays the restaurants menu options to the user.

    This function prints the restaurants menu options available to the user,
    allowing them to select an option to proceed further.
    """

    print(Cor.CIANO + "=" * 55 + Cor.RESET)
    print("\n[MENU DE RESERVAS]\n")
    print("1. ADICIONAR RESTAURANTE")
    print("2. LISTAR RESTAURANTES")
    print("3. ALTERAR INFORMAÇÕES DO RESTAURANTE")
    print("4. DELETAR RESTAURANTE")
    print("5. VOLTAR AO MENU ANTERIOR")
    print(Cor.CIANO + "=" * 55 + Cor.RESET)


def administra_opcoes_menu_reserva():
    """
    Handles the reservation options by presenting the user with a menu
      and performing actions based on their choice.

    This function continuously displays the reservation menu
      until the user chooses to return to the previous menu.
    It allows users to make a reservation, list reservations,
      update reservation details, cancel a reservation,
      verify a reservation, or return to the previous menu.
    """

    while True:
        menu_reservas()
        opcao_main = int(input("ESCOLHA UMA OPÇÃO: "))

        if opcao_main == 1:
            nome_restaurante = input("Qual o nome do restaurante? ")
            nome = input("Qual o nome do responsável pela reserva? ")
            cpf = int(input("Informe o seu CPF: "))
            data = input("Qual a data da reserva? ")
            qtd_pessoas = int(input("Reserva para quantas pessoas? "))
            horario = input("Digite o horário que você deseja: ")
            mesa = int(input("Qual o número da mesa que você deseja? "))

            reservas.reservar(
                nome_restaurante,
                nome,
                cpf,
                data,
                qtd_pessoas,
                horario,
                mesa,
            )

        elif opcao_main == 2:
            reservas.listar_reservas()

        elif opcao_main == 3:
            cpf = int(input("Informe o CPF cadastrado na reserva: "))
            nova_data = input("Digite a nova data: ")
            novo_horario = input("Digite o novo horário: ")
            reservas.atualizar_reserva(cpf, nova_data, novo_horario)

        elif opcao_main == 4:
            cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
            reservas.cancelar_reserva(cpf)

        elif opcao_main == 5:
            cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
            reservas.verificar_reserva(cpf)

        elif opcao_main == 6:
            print("VOLTAR AO MENU ANTERIOR...")
            sleep(3)
            break
        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


def administra_opcoes_menu_restaurante():
    """
    Handles the restaurant options by presenting the user with a menu
    and performing actions based on their choice.

    This function continuously displays the restaurant menu
    until the user chooses to return to the previous menu.
    It allows users to add a restaurant, list restaurants,
    update restaurant information, delete a restaurant,
    or return to the previous menu.
    """

    while True:
        menu_restaurantes()
        opcao_main = input("ESCOLHA UMA OPÇÃO: ")

        if opcao_main == "1":
            nome = input("Qual o nome do restaurante? ")
            informacoes = input(
                "Digite informações sobre o tipo de cardápio do restaurante "
                "(Churrascaria, comida japonesa etc): "
            )
            endereco = input("Qual o endereço? ")
            funcionamento = input("Qual o horário de funcionamento? ")
            avaliacao = int(input("Digite a avaliação do restaurante (0-5): "))

            restaurantes.adicionar_restaurante(
                nome, endereco, informacoes, funcionamento, avaliacao
            )

        elif opcao_main == "2":
            restaurantes.listar_restaurantes()

        elif opcao_main == "3":
            nome_atual = input(
                "Digite o nome do restaurante que você deseja atualizar: "
            )
            print(
                "Caso você não deseje atualizar um campo qualquer,"
                " por exemplo o nome, apenas repita o nome já existente, e assim sucessivamente.\n"
            )

            novo_nome = input("Qual o novo nome do restaurante? ")
            novas_informacoes = input("Novas informações: ")
            novo_endereco = input("Qual o novo endereço? ")
            novo_funcionamento = input("Qual o novo horário de funcionamento? ")
            nova_avaliacao = int(input("Qual a nova avaliação do restaurante: "))
            restaurantes.atualizar_restaurantes(
                nome_atual,
                novo_nome,
                novas_informacoes,
                novo_endereco,
                novo_funcionamento,
                nova_avaliacao,
            )

        elif opcao_main == "4":
            nome = input(
                "Digite o nome do restaurante que será excluído do sistema:\n>>>"
            )
            restaurantes.excluir_restaurante(nome)

        elif opcao_main == "5":
            print("VOLTAR AO MENU ANTERIOR...")
            sleep(3)
            break
        else:
            print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


def verificar_e_notificar_reservas():
    reservas_proximas = reservas.reservas_proximas()

    if reservas_proximas:
        print("Reservas próximas:")
        for reserva in reservas_proximas:
            print(
                "Você tem reservas próximas: \n"
                f"Restaurante: {reserva['nome_restaurante']}, Data: {reserva['data']}, Horário: {reserva['horario']}"
            )
    else:
        print("Não há reservas próximas.")


def main():
    """
    Main function to run the application.

    This function displays the initial menu to the user and processes their choice.
    It handles all the core logic of the application, including displaying menus,
    processing user inputs, and calling appropriate functions based on the user's choices.
    """

    while True:
        menu_inicial()
        primeiro_menu = int(input("INFORME UMA OPÇÃO: \n"))

        match (primeiro_menu):
            case 1:
                administra_opcoes_menu_reserva()

            case 2:
                administra_opcoes_menu_restaurante()

            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")


if __name__ == "__main__":
    verificar_e_notificar_reservas()
    main()
