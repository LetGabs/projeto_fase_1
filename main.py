
#SISTEMA DE GERENCIAMENTO HOSPITALAR
import funcoes

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
            funcoes.adicionar_paciente()
        elif opcao == 2:
            funcoes.adicionar_medico()
        elif opcao == 3:
            funcoes.pesquisar_paciente()
        elif opcao == 4:
            funcoes.pesquisar_medico()
        elif opcao == 5:
            funcoes.excluir_paciente()
        elif opcao == 6:
            funcoes.excluir_medico()
        elif opcao == 7:
            funcoes.sair()
        else:
            print("Opção inválida. TENTE NOVAMENTE!")

if __name__ == "__main__":
    menu()
