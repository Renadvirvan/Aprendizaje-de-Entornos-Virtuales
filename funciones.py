def calculo(nmat):
    calif = []
    sumM = 0

    for i in range(0,nmat):
        calif.append(int(input("Calificacion de la materia "+str(i+1)+"?: ")))

    for i in calif:
        sumM += i
    return (sumM/nmat)

def menu():
    valRef = True
    while valRef:
        nmat = int(input("Bienvenido, cuantas materias tienes?:\n"))
        prom = calculo(nmat)
        print("Tu promedio es: "+ str(prom))
        if(input("Desea continuar?\n 1.Si\n 2.No\n") == '2'):
            valRef = False

def main():
    menu()

main()