
#SISTEMA DE GERENCIAMENTO HOSPITALAR

from funcoes import adicionar_paciente
from funcoes import adicionar_medico
from funcoes import pesquisar_paciente
from funcoes import pesquisar_medico
from funcoes import excluir_paciente
from funcoes import excluir_medico
from funcoes import sair

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
            adicionar_medico()
        elif opcao == 3:
            pesquisar_paciente()
        elif opcao == 4:
            pesquisar_medico()
        elif opcao == 5:
            excluir_paciente()
        elif opcao == 6:
            excluir_medico()
        elif opcao == 7:
            sair()
        else:
            print("Opção inválida. TENTE NOVAMENTE!")

if __name__ == "__main__":
    menu()
