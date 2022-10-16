def menu():
    si = True
    while (si):
        tamTabla = int(input("Ingrese el tamano de entradas:  "))
        matrix = drawTabla(tamTabla)
        elecc = input("1) AND\n2) OR\n")
        if (elecc == '1'):
            AND = calAND(matrix)
            drawRes(AND, matrix, "AND")            
        elif (elecc == '2'):
            OR = calOR(matrix)
            drawRes(OR, matrix, "OR")            
        entrada = int(input("1) Bye bye :)\n2) Continuar\n"))
        if(entrada == 1):
            si = False
            print("\nBye bye, vuelva pronto :3\n")        


def drawTabla(tamTabla):
    res = 2**tamTabla
    fila = []
    matrix = []

    for i in range(0, res):
        volBin = format(i, "=b")
        if (len(volBin) < tamTabla):
            aux = tamTabla - len(volBin)
            for j in range(0, aux):
                fila.append('0')
        for j in volBin:
            fila.append(j)
        matrix.append(fila)
        fila = []
    return matrix

def calAND(matrix):
    AND = []
    # Sacando el opereador and
    for i in matrix:
        if (i.count('0')):
            AND.append('0')
        else:
            AND.append('1')
    return AND

def calOR(matrix):
    OR = []
    for i in matrix:
        if (i.count('1')):
            OR.append('1')
        else:
            OR.append('0')
    return OR

def drawRes(Vec, matrix, OPC):
    print("\nTabla de verdad de la" + OPC)
    item = 0
    for i in matrix:
        if(OPC.count('O')):
            print("\t" + str(i) + "[" +str(Vec[item]) + "]")
        else:
            print("\t" + str(i) + "[" +str(Vec[item]) + "]")
        item += 1

menu()