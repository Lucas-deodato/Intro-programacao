import json
import os

arquivo = os.path.join(os.path.dirname(__file__), 'reservas.json')

#CREATE: CRIAR RESERVA
def reservar(nome_restaurante, nome, cpf, data, qtd_pessoas, horario, mesa):
    with open(arquivo, 'r') as f:
        reserva = json.load(f)

    reserva.append({
        "nome-restaurante": nome_restaurante,
        "nome": nome,
        "cpf": cpf,
        "data": data,
        "pessoas": qtd_pessoas,
        "horario": horario,
        "mesa": mesa
    })

    with open(arquivo, 'w') as f:
        json.dump(reserva, f, indent=4)

    print("😎 RESERVA CONFIRMADA!")

#READ: LER TODAS AS RESERVAS
def listar_reservas():
    with open(arquivo, 'r') as f:
        reservas = json.load(f) 

    if reservas: 
        print("=" *50)
        print("RESERVAS:")
        print("-" *50)
        for r in reservas:
            print("*" *35)
            print(f"Restaurante: {r['nome-restaurante']}\nHorário: {r['horario']}\nMesa: {r['mesa']}")
            print("*" *35)
    else:
        print("NENHUMA RESERVA EFETUADA AINDA, TODOS OS HORÁRIOS ESTÃO DISPONÍVEIS.")

#UPDATE: ATUALIZAR O HORÁRIO DA RESERVA
def atualizar_reserva(cpf, nova_data, novo_horario):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:
        if r['cpf'] == cpf:
            r['horario'] = novo_horario
            r['data'] = nova_data

            with open(arquivo, 'w') as f:
                json.dump(reservas, f, indent=4)

            print("😙 HORÁRIO DA RESERVA ATUALIZADO COM SUCESSO!!")
            break
        else:
            print('O CPF não consta na lista de reservas.')

#DELETE: CANCELAR A RESERVA
def cancelar_reserva(cpf):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:  
        if r['cpf'] == cpf:
            reservas.remove(r)

            with open(arquivo, 'w') as f:
                json.dump(reservas, f, indent=4)
            
            print("😡 RESERVA CANCELADA COM SUCESSO!")
            break
        else:
            print('O CPF não consta na lista de reservas.')

# VERIFICAR APENAS A SUA RESERVA
def verificar_reserva(cpf):
    with open(arquivo, 'r') as f:
        reservas = json.load(f)

    for r in reservas:
        if r['cpf'] == cpf:
            print("--- Dados da reserva ---\n")
            print(f"Nome: {r['nome']}\nCPF: {r['cpf']}\nData: {r['data']}\nN° de pessoas: {r['pessoas']}\nHorário: {r['horario']}\nMesa: {r['mesa']}")
            break
        else:
            print("Reserva não encontrada.")