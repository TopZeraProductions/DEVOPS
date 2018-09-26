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


def adicionar():
	print("Adicionar um registro")
	agenda = open("agendatelefonica.csv",'a')
	nome = input("Nome do Contato:").lower()
	telefone = input("Digite o telefone:")
	print("Contato salvo com nome:",nome," e numero",telefone)
	agenda.write(nome + ", " + telefone+"\n")
	agenda.close()

def listar():
	array = readCSV()
	for index, item in enumerate(array):
		print(index, " - ", array[index])


def buscar(valor):
	ListaAgenda = readCSV()

	resposta = {}
	for index, item in enumerate(ListaAgenda):
		nome , numero = ListaAgenda[index].split(",")
		if valor in ListaAgenda[index]:
			resposta[index] = nome

	return resposta

def buscaNome(value):
	response = buscar(value.lower())
	if len(response) > 0 :
		print("Foram encontrados ",len(response),"iguais a " + value + " resultados:")

		for key in response:
			print(key, " - ", response[key])

	else:
		print("Não foram encontrados valores")

def delete(value):
	array = readCSV()
	response = buscar(value.lower())

	if len(response) > 0:
		print("Foram encontrados ", len(response), "iguais a " + value + " resultados:")
		for key in response:
			print(key, " - ", response[key])

		opt = int(input("Digite o ID que vc queira deletar"))

		array.pop(opt)
		writeCSV(array)

	else:
		print("Não foram encontrados valores")

def readCSV():
	with open("agendatelefonica.csv") as agenda:
		return agenda.readlines()

def writeCSV(array):
	with open("agendatelefonica.csv", 'w') as agenda:
		for item in array:
			agenda.write(item.lower())
			
