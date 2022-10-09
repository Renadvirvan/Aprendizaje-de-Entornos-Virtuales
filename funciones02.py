def promParcial():
    califPar = []
    for i in range(0,3):
        califPar.append(float(input("Ingresa tu calificacion del parcial "+str(i+1)+"\n")))

    promParMat = 0
    for j in califPar:
        promParMat += j        
    return (promParMat/3)

def promGeneral(nmat):
    califMat = []
    for i in range(0,nmat):
        print("Calificaciones de la materia "+str(i+1))
        califMat.append(promParcial())

    sumM = 0
    for i in califMat:
        sumM += i
    return(sumM/nmat)
    

def main(): 
    
    acc = True
    while(acc):
        nmat =int(input("Bienvenido, cuantas materias tienes?:\n"))
        resultProm = promGeneral(nmat)
        print("Tu Promedio escolar fue: "+str(resultProm))
        if(input("Le gustaria continuar? \n1) Si\n2)No\n") == '2'):
            acc = False

main()