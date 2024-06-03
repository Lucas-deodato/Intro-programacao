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


arquivo = os.path.join(os.path.dirname(__file__), 'reservas.json')


def limpar_tela():
    os.system('cls')

# CREATE
def reservar(nome, cpf, data, qtd_pessoas, horario, mesa):
    with open(arquivo, 'r') as f:
        info_reserva = json.load(f)

    info_reserva.append({
        "nome": nome,
        "cpf": cpf,
        "data": data,
        "pessoas": qtd_pessoas,
        "horario": horario,
        "mesa": mesa
    })

    with open(arquivo, 'w') as f:
        json.dump(info_reserva, f, indent=4)

    print("😎 RESERVA CONFIRMADA!")


def listar_reservas():
    with open(arquivo, 'r') as f:
        reservas = json.load(f) 

    if reservas: 
        print("=" *50)
        print("RESERVAS:")
        print("-" *50)
        for r in reservas:
            print("*" *35)
            print(f"Nome: {r['nome']}\nData: {r['data']}\nN° de pessoas: {r['pessoas']}\nHorário: {r['horario']}\nMesa: {r['mesa']}\nID da reserva: {r['cpf']}")
            print("*" *35)
            print("=" *35)
    else:
        print("NENHUMA RESERVA EFETUADA AINDA, TODOS OS HORÁRIOS ESTÃO DISPONÍVEIS.")


def atualizar_reserva(cpf, novo_horario):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:
        if r['cpf'] == cpf:
            r['horario'] = novo_horario
            break

    with open(arquivo, 'w') as f:
        json.dump(reservas, f, indent=4)
    print("😙 HORÁRIO DA RESERVA ATUALIZADO COM SUCESSO!!")


def cancelar_reserva(cpf):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:  
        if r['cpf'] == cpf:
            reservas.remove(r)
        else:
            print('O CPF não consta na lista de reservas.')

    with open(arquivo, 'w') as f:
        json.dump(reservas, f, indent=4)
        print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")


def verificar_reserva(cpf):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:
        if r['cpf'] == cpf:
            print(f"--- Dados da reserva ---\n{r}")
        else:
            print(cpf)
            print("Reserva não encontrada.")


def menu_inicial():
    print (Cor.CIANO + "=" *55 + Cor.RESET)
    print ("          1 - MENU DE RESERVAS")
    print ("          2 - LISTAR RESTAURANTES")
    print ("          3 - SAIR ")
    print (Cor.CIANO + "=" *55 + Cor.RESET)


def main_menu():
    print (Cor.CIANO + "=" *55 + Cor.RESET)
    print("\n[MENU DE RESERVAS]\n")
    print("1. FAZER RESERVA")  #crete
    print("2. LISTAR RESERVAS")  # read all
    print("3. ALTERAR HORÁRIO DA RESERVA")  # update
    print("4. CANCELAR RESERVA")  # delete
    print("5. VERIFICAR INFORMAÇÕES DA RESERVA")  # read
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

                        reservar(nome, cpf, data, qtd_pessoas, horario, mesa)
                
                    elif opcao_main == "2":
                        listar_reservas()

                    elif opcao_main == "3":
                        cpf = int(input("Informe o CPF cadastrado na reserva: "))
                        novo_horario = input("Digite o novo horário: ")
                        atualizar_reserva(cpf, novo_horario)

                    elif opcao_main == "4":
                        cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
                        cancelar_reserva(cpf)

                    elif opcao_main == "5":
                        cpf = int(input("Digite o CPF cadastrado na reserva:\n>>>"))
                        verificar_reserva(cpf)

                    elif opcao_main == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()