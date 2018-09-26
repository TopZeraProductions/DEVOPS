def adicionar(nome, telefone):
    if len(nome) > 20 or len(nome) < 10 or len(telefone) > 11 or len(telefone) < 11:

        return False

    try:
        intTel = int(telefone)

        agenda = open("agendatelefonica.csv", 'a')
        agenda.write(nome.lower() + ", " + telefone + "\n")
        agenda.close()

        return True
    except:

        return False


def listar():
    try:
        array = readCSV()
        for index, item in enumerate(array):
            print(index, " - ", array[index])

        return True

    except:
        return False


def buscar(valor):
    ListaAgenda = readCSV()
    valor = valor.lower()
    resposta = {}

    try:

        for index, item in enumerate(ListaAgenda):
            nome, numero = ListaAgenda[index].split(",")
            if valor in ListaAgenda[index]:
                resposta[index] = nome
        return resposta
    except ValueError:
        return {}


def buscaNome(value):
    response = buscar(value.lower())
    if len(response) > 0:
        print("Foram encontrados ", len(response), "iguais a " + value + ", resultados:")

        for key in response:
            print(key, " - ", response[key])

    else:
        print("Não foram encontrados valores")

def delete(value):
    array = readCSV()
    response = buscar(value.lower())

    if len(response) > 0:
        print("Foram encontrados ", len(response), "iguais a " + value + ", resultados:")

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
