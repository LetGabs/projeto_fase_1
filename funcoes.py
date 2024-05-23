import time
pacientes = []
medicos = []

def adicionar_paciente():
    cpf = input('Digite o CPF: ').strip()
    nome = input('Digite o nome: ').strip()
    idade = input('Digite a idade: ').strip()
    endereco = input('Digite o endereço: ').strip()
    celular = input('Digite o número para contato: ').strip()

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
    nome = input('Digite o nome: ').strip()
    especialidade = input('Digite a especialidade do médico: ').strip()
    crm = input('Digite o CRM: ').strip()
    celular = input('Digite o número para contato: ').strip()

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
    cpf = input('Digite o CPF do paciente a ser pesquisado: ').strip()
    for paciente in pacientes:
        if paciente["CPF"] == cpf:
            time.sleep(1)
            print (f"Nome: {paciente['Nome']}\n CPF: {paciente['CPF']}, \n Endereço: {paciente['Endereco']}, \n Telefone: {paciente['Celular']}")
            time.sleep(1)
            return
        print("Paciente não encontrado! ")
def pesquisar_medico():
    crm = input('Digite o CRM do médico: ').strip()
    for medico in medicos:
        if medico["CRM"] == crm:
            time.sleep(1)
            print (f"Nome: {medico['Nome']}\n CRM: {medico['CRM']} \n Especialidade: {medico['Especialidade']} \n Telefone: {medico['Celular']}")
            time.sleep(1)
            return
        print("Medico não encontrado!")
def excluir_paciente():
    cpf = input("Digite o CPF do PACIENTE que deseja excluir: ").strip()
    for paciente in enumerate(pacientes):
        if paciente["CPF"] == cpf:
            del pacientes[paciente]
            print("Paciente excluído com sucesso!")
            return
        print("Paciente não encontrado!")

def excluir_medico():
    crm = input("Digite o CRM do MÉDICO que deseja excluir: ").strip()
    for medico in enumerate(medicos):
        if medico["CRM"] == crm:
            del medicos[medico]
            print("Médico excluído com sucesso!")
            return
        print("Médico não encontrado!")

def sair():
    print("Encerrando sistema...")
    exit()