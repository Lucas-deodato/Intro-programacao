import json
import os
from time import sleep
import reservas

class Cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo = os.path.join(os.path.dirname(__file__), 'reservas.json')


def menu_inicial():
    print (Cor.CIANO + "=" *55 + Cor.RESET)
    print ("          1 - MENU DE RESERVAS")
    print ("          2 - LISTAR RESTAURANTES")
    print ("          3 - SAIR ")
    print (Cor.CIANO + "=" *55 + Cor.RESET)


def main_menu():
    print (Cor.CIANO + "=" *55 + Cor.RESET)
    print("\n[MENU DE RESERVAS]\n")
    print("1. FAZER RESERVA") 
    print("2. LISTAR RESERVAS")
    print("3. ALTERAR DATA/HORA DA RESERVA")
    print("4. CANCELAR RESERVA")
    print("5. VERIFICAR INFORMAÇÕES DA SUA RESERVA")
    print("6. VOLTAR AO MENU ANTERIOR")
    print (Cor.CIANO + "=" *55 + Cor.RESET)


def main():
    while True:
        menu_inicial()
        primeiro_menu = int(input("INFORME UMA OPÇÃO: "))

        match (primeiro_menu):
            case 1:  
                while True: 
                    main_menu()
                    opcao_main = input("ESCOLHA UMA OPÇÃO: ")

                    if opcao_main == "1":
                        nome = input("Qual o nome do responsável pela reserva? ")
                        cpf = int(input("Informe o seu CPF: "))
                        data = input("Qual a data da reserva? ")
                        qtd_pessoas = int(input("Reserva para quantas pessoas? "))
                        horario = input("Digite o horário que você deseja: ")
                        mesa = int(input("Qual o número da mesa que você deseja? "))

                        reservas.reservar(nome, cpf, data, qtd_pessoas, horario, mesa)
                
                    elif opcao_main == "2":
                        reservas.listar_reservas()

                    elif opcao_main == "3":
                        cpf = int(input("Informe o CPF cadastrado na reserva: "))
                        nova_data = input("Digite a nova data: ")
                        novo_horario = input("Digite o novo horário: ")
                        reservas.atualizar_reserva(cpf, nova_data, novo_horario)

                    elif opcao_main == "4":
                        cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
                        reservas.cancelar_reserva(cpf)

                    elif opcao_main == "5":
                        cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
                        reservas.verificar_reserva(cpf)

                    elif opcao_main == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("LISTA DE RESTAURANTES")

            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()