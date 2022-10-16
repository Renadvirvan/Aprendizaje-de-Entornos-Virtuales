tamTabla = int(input("Ingrese el tamano de entradas:  "))
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
#print(matrix)
AND = []
OR = []
# Sacando el opereador and
for i in matrix:
    if (i.count('0')):
        AND.append('0')
    else:
        AND.append('1')

print("\nTabla de verdad de la AND")
item = 0
for i in matrix:
    print("\t" + str(i) + "[" +str(AND[item]) + "]")
    item += 1

# Sacando el opereador or
for i in matrix:
    if (i.count('1')):
        OR.append('1')
    else:
        OR.append('0')

print("\nTabla de verdad de la OR")
item = 0
for i in matrix:
    print("\t" + str(i) + "[" +str(OR[item]) + "]")
    item += 1
