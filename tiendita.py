tiendita = {
    "productos": {
        "peluches": 75,
        "dulces": 15,
        "muñecas": 235,
        "compus": 15000,
        "cafe": 25,
        "patines": 2300  
    },
    "empleados":{
        "empleado1": {
            "nombre": "Dulce Maria",
            "edad": 25,
            "estadoCivil": "Mimada y mantenida" 
        },
        "empleado2": {
            "nombre": "Jorge Triviño",
            "edad": 19,
            "estadoCivil": "Comprometido" 
        }
    }
}

print(tiendita["empleados"]["empleado1"]["nombre"])
nom = input("Hola, bienvenido a la tiendita 'LOCA'\nCual es tu nombre?:\n")

compras = "no"
while compras == "no" or compras2 == "si":
    print("\nHola "+nom+", nuestros productos son los siguientes: \n")
    print(tiendita["productos"])

    art = input("Cual articulo te interesa?: \n")
    if (art == "peluches"):
        respues = input("Su costo es de: "+str(tiendita["productos"]["peluches"])+"\nDeseas agregarlo al carrito?:\n") #dfsdffd
        if (respues == "si"):
            compras = input("Se ha agregado este articulo a su carrito\nDesea salir, y pagar ahorita?: \n")
        else:
            print("Muchas gracias por su compra, que disfrute de su dia y su articulo "+nom)
            #dgdfg pago
    else:
        compras2 = input("Perfecto "+nom+",desea seguir comprando?:\n")
        if(compras2 == "no"):
            print("Muchas gracias por su visita"+nom+",que disfrute de su dia")
    elif (art == "dulces"):
        respues = input("Su costo es de: "+str(tiendita["productos"]["dulces"])+"\nDeseas comrarlo?:\n")
        if (respues == "si"):
            compras = input("Se ha agregado este articulo a su carrito\nDesea seguir comprando?: \n")
