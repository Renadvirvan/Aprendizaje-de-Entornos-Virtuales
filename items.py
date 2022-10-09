# Contador/ Identificador/ Item Ejercicio 1 :)
vec = [5, 6, 8, 9, 4, 4, 3, 2]
item = 0
for i in vec:
    if(i == 4):
        item += 1

print("Existe "+str(item)+" cuatros\n")
print("\nAveriguemos si estuvo bien hecho :))")

# Contador/ Identificador/ Item Ejercicio 2 :)
print("\n"+str(vec.count(4))+"\n")

# Contador/ Identificador/ Item Ejercicio 3 :)
if(vec.count(9)):
    for i in vec:
        print("\n"+str(i)+"\n")
        if(i==9):
            break

# Contador/ Identificador/ Item Ejercicio 4 :)
for i in range(0,4):
    print("\n"+str(vec[i])+"\n")

# Contador/ Identificador/ Item Ejercicio 5 :)
print(vec[:vec.index(8)+1])

# Contador/ Identificador/ Item Ejercicio 6 :)
sum = 0
for i in vec:
    if(i!=8):
        sum  += i
print("\n"+str(sum)+"\n")


# Contador/ Identificador/ Item Ejercicio 7 :)
nmat =int(input("Bienvenido, cuantas materias tienes?:\n"))

califMat = []
for i in range(0,nmat):
    print("Calificaciones de la materia "+str(i+1))
    califPar = []
    for j in range(0,3):
        califPar.append(int(input("Ingresa tu calificacion del parcial "+str(j+1)+"\n")))

    promParMat = 0
    for j in califPar:
        promParMat += j        
    califMat.append(promParMat/3)

sumM = 0
for i in califMat:
    sumM += i
prom = sumM/nmat
print("\n"+str(prom)+"\n")