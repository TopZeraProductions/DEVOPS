import funcoes
import sys

def readCSV():
    with open("agendatelefonica.csv") as agenda:
        return agenda.readlines()

def writeCSV(array):
    with open("agendatelefonica.csv", 'w') as agenda:
        for item in array:
            agenda.write(item.lower())

def testADD():
    print("testADD >>>")
    success = 0

    # get data before changes
    array = readCSV()
    # get data before changes

    listOfDict = [
          {"testName": "TEST1-KHDIHDIHDHHDHD"  , "testTelfone": "11222233334" , "expected" : True  }
        , {"testName": "TEST2-HDIHDIHDHHDHDHH" , "testTelfone": "11222233334" , "expected" : False }
        , {"testName": "TEST3-KHDIHDIHDHHDHDH" , "testTelfone": "111222233334", "expected" : False }
        , {"testName": "TEST5"                 , "testTelfone": "11122223333" , "expected" : False }
        , {"testName": "TEST6-IHDIHDIHDHHDHDH" , "testTelfone": "11122223333" , "expected" : False }
    ]


    index = 0
    for dict in listOfDict:

        index += 1
        ret = funcoes.adicionar(dict["testName"], dict["testTelfone"])

        if ret == dict["expected"] :
            print(("{}st case successfully response: {}").format(index, ret))
        else:
            success += 1
            print(("{}st case failure response: {}").format(index, ret))


    #restoring data after changes
    writeCSV(array)
    #restoring data after changes

    if success > 0:
        print("\nError!!!")
        sys.exit(1)


def testSerched():
    print("testSearch >>>")
    fails = 0

    #list befor changes
    before =  readCSV()
    #list before changes

    listOfDict = [
          {"testName": "TEST1-KHDIHDIHDHHDH"  , "testTelfone" : "11222233334" , "expected" : True}
        , {"testName": "TEST2-HDIHDIHDHHDHDHH", "testTelfone" : "11222233334" , "expected" : False}
        , {"testName": "TEST3-HD,IHDIHDHHDHD" , "testTelfone" : "11222233334" , "expected" : False}
        , {"testName": "TEST3-HDIHDIHDHHDHD"  , "testTelfone" : "11,222233334", "expected" : False}
    ]

    index = 0
    for dict in listOfDict:

        index += 1
        funcoes.adicionar(dict["testName"], dict["testTelfone"])

        retorno = funcoes.buscar(dict["testName"])

        if len(retorno) > 0 :

            print(("{}st case successfully ").format(index))
        elif dict["expected"] == False:

            print(("{}st case successfully ").format(index))
        else:
            fails += 1
            print(("{}st case failure ").format(index))


    # restoring data after changes
    writeCSV(before)
    # restoring data after changes

    if fails > 0:
        print("\nError!!!")
        sys.exit(1)


testADD()
testSerched()

print("\nAll OK!!!")
sys.exit(0)