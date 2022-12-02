


objetos = {
    "escudo de doran" : {
        "valor" : 200
    },
    "espada de doran" :{
        "valor" : 100
    },
    "espada de granizo" : {
        "valor" : 140
    },
    "cuchilla de ascuas" : {
        "valor" : 350
    },
    "preferencia" : {
        "valor" : 50
    },
    "anillo de doran" : {
        "valor" : 350
    },
    "sello oscuro" : {
        "valor" : 250
    },
        
}

campeon="Lee sin"

monedas = 500

inventario=["smite","potion"]

x = input(str(f"Hola {campeon}, ¿qué deseas comprar?\n"))

if x in objetos : 
    print("Su valor es de")
    print(objetos[x]["valor"])
    #print(objetos.get(x)) - Prueba que no ha salido bien

    y = input(str("¿Estás seguro que deseas comprar este objeto? ¿Si o no?\n"))
    
    if y == "si" :
        r = (objetos[x]["valor"])
        z = monedas - r
        inventario.append(x)
        print(f"Gracias por tu compra, tu saldo ahora mismo es de {z} y actualmente tu inventario consta de {inventario}" )
        #inventario.append(x) - Lo habia hecho en dos pasos pero mas facil todo en una frase
        #print(f"Actualmente tu inventario consta de {inventario}")
    
    elif y == "no" :
        print("De acuerdo, hasta pronto")
    
    else :
        print("Lo siento, no te he entendido")
        

else :
    print("Lo siento, no dispongo de este objeto")


# Pruebas 
#for x in objetos : 
    #print(x)

#key = objetos.keys()

#for x in objetos :
    #print(objetos["x"])