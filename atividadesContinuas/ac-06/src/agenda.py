#Agenda Telefonica
import funcoes

def add():
    print("---Adicionar um registro---\nNomes 10 e 20 caracteres e numeros de telefone validos")

    nome = input("Nome do Contato:").lower()
    telefone = input("Digite o telefone:")

    if funcoes.adicionar(nome, telefone):
        print("Contato salvo com nome:", nome, " e numero", telefone)
    else:
        print("Erro, verifique os dados ou contate o suporte tecnico")

def bemvindo():
	print("\n--------------Agenda v0.1----------------\n")
	print("Selecione uma Opcao")
	print("1 - Adicionar um novo contato")
	print("2 - Listar os contatos da agenda")
	print("3 - buscar um contato")
	print("4 - Deletar um contato")
	print("qualquer outra tecla para sair")

def sair():
    print("saindo...")
    exit()

while 1:

    bemvindo()

    opcao = input()

    #opcao = ""
    if opcao == "1":
        add()

    elif opcao == "2":
        funcoes.listar()
    elif opcao == "3":
        funcoes.buscaNome(input("Digite o contato: "))
    elif opcao == "4":
        funcoes.delete(input("Digite o contato: "))
    else:
        sair()

