import time
#SISTEMA DE GERENCIAMENTO HOSPITALAR

pacientes = []
medicos = []

def adicionar_paciente():
    cpf = input('Digite o CPF: ')
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    endereco = input('Digite o endereço: ')
    celular = input('Digite o número para contato: ')

# condicional para permitir que o programa só siga se todos os dados forem preenchidos
    if not cpf or not nome or not idade or not endereco or not celular:
        print("Por favor, preencha todos os campos obrigatórios.")

# verificar se o paciente já está cadastrado no sistema
    for paciente in pacientes:
        if paciente["CPF"] == cpf:
            print("ERRO: Paciente já cadastrado!")
            return
    novo_paciente ={
        "CPF": cpf, "Nome": nome, "Idade": idade, "Endereco": endereco, "Celular": celular
    }
    pacientes.append(novo_paciente)
    print("Paciente adicionado com sucesso!")

def adicionar_medico():
    nome = input('Digite o nome: ')
    especialidade = input('Digite a especialidade do médico: ')
    crm = input('Digite o CRM: ')
    celular = input('Digite o número para contato: ')
    # condicional para permitir que o programa só siga se todos os dados forem preenchidos
    if not nome or not crm or not especialidade or not celular:
        print("Por favor, preencha todos os campos obrigatórios.")

    # verificar se o médico já está cadastrado no sistema
    for medico in medicos:
        if medico["CRM"] == crm:
            print("ERRO: Médico já cadastrado!")
            return
    novo_medico = { "Nome": nome, "Especialidade": especialidade, "CRM": crm, "Celular": celular
    }
    medicos.append(novo_medico)
    print("Medico adicionado com sucesso!")

def pesquisar_paciente():
    cpf = input('Digite o CPF do paciente a ser pesquisado: ')
    for paciente in pacientes:
        if paciente["CPF"] == cpf:
            time.sleep(1)
            print (f"Nome: {paciente['Nome']}\n CPF: {paciente['CPF']}, \n Endereço: {paciente['Endereco']}, \n Telefone: {paciente['Celular']}")
            time.sleep(1)
            return
        print("Paciente não encontrado! ")
def pesquisar_medico():
    crm = input('Digite o CRM do médico: ')
    for medico in medicos:
        if medico["CRM"] == crm:
            time.sleep(1)
            print (f"Nome: {medico['Nome']}\n CRM: {medico['CRM']} \n Especialidade: {medico['Especialidade']} \n Telefone: {medico['Celular']}")
            time.sleep(1)
            return
        print("Medico não encontrado!")
def excluir_paciente():
    cpf = input("Digite o CPF do PACIENTE que deseja excluir: ")
    for paciente in enumerate(pacientes):
        if paciente["CPF"] == cpf:
            del pacientes[paciente]
            print("Paciente excluído com sucesso!")
            return
        print("Paciente não encontrado!")

def excluir_medico():
    crm = input("Digite o CRM do MÉDICO que deseja excluir: ")
    for medico in enumerate(medicos):
        if medico["CRM"] == crm:
            del medicos[medico]
            print("Médico excluído com sucesso!")
            return
        print("Médico não encontrado!")

def sair():
    print("Encerrando sistema...")
    exit()

def menu():
    while True:
        print("\n -----> BEM VINDO AO PROGRAMA DE GERENCIAMENTO HOSPITALAR <-----")
        print()
        print ("======> MENU <======")
        print("1 - ADICIONAR NOVO PACIENTE")
        print("2 - ADICIONAR NOVO MÉDICO")
        print("3 - PESQUISAR PACIENTE POR CPF")
        print("4 - PESQUISAR MÉDICO POR CRM")
        print("5 - EXCLUIR PACIENTE PELO CPF")
        print("6 - EXCLUIR MÉDICO PELO CRM")
        print("7 - SAIR DO SISTEMA")
        opcao = int(input("\n-----------> Digite a opção desejada: "))

        if opcao == 1:
            adicionar_paciente()
        elif opcao == 2:
            adicionar_paciente()
        elif opcao == 3:
            pesquisar_paciente()
        elif opcao == 4:
            pesquisar_paciente()
        elif opcao == 5:
            excluir_paciente()
        elif opcao == 6:
            excluir_paciente()
        elif opcao == 7:
            sair()
        else:
            print("Opção inválida. TENTE NOVAMENTE!")

if __name__ == "__main__":
    menu()
