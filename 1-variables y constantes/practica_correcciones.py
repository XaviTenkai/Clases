'''
Primero las estructuras de código (variables, listas, tuplas, diccionarios...)

TAREA: Poner todo lo que se pueda repetir o ser suceptible de repetir con alguna pequeña modificación en funciones

TAREA 2: Poner el menú de una forma en la que si el usuario teclear salir salga de la aplicación y si no, una vez ejecute la acción que quiera ejecutar

retornarlo de nuevo al menú principal.

'''

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

# Creando campeon

campeon="Lee sin"

# Creando saldo del campeon

monedas =  500

saldo_restante = 0

# Creando inventario del campeon

inventario=["smite","potion"]

# Creando la primera pregunta para saber qué desea comprar

print(f"\nHola {campeon}, dispongo de los siguientes objetos: ", end="" )

print(str(objetos.keys()).replace("{","").replace("}", "").replace("'", "").replace("[","").replace("]","").replace("dict_keys","").replace("(","").replace(")",""))

compra = input(str("\n¿Qué deseas comprar?\n"))

def objeto_que_se_quiere_comprar(nombre_del_objeto):
    print("\nLo siento no te he entendido, ¿puedes volver a repetirlo?")

    compra = input(str("\n¿Qué deseas comprar?\n"))


    if compra.lower in objetos :
        return True   
    return False

while compra.lower() not in objetos :

    if objeto_que_se_quiere_comprar(compra):
        break

print(f"\nEl valor de {compra.lower()} es de:",end=" ")

print (objetos[compra.lower()]["valor"])

saldo_restante = int(objetos[compra.lower()]["valor"])

afirmacion = ["si"]

pregunta_2 = input(str("\n¿Estás seguro que deseas comprarlo?\n"))

#bolsa = monedas - saldo_restante

monedas = 500

bolsa = monedas - saldo_restante

inventario.append(compra)

if pregunta_2.lower() in afirmacion :
    
    pregunta_3 = (input(str(f"\nDe acuerdo, tu saldo actual es de {bolsa} y tu inventario consta de {inventario}, ¿deseas comprar algo más?\n")))
    
    if pregunta_3.lower() in afirmacion :
    
        while bolsa >= 0 :

            compra = input(str("\n¿Qué deseas comprar?\n"))
            
            while compra.lower() not in objetos :

                print("\nLo siento no te he entendido, ¿puedes volver a repetirlo?")

                compra = input(str("\n¿Qué deseas comprar?\n"))

            if compra.lower in objetos :

                break

            monedas = bolsa
                
            saldo_restante = int(objetos[compra.lower()]["valor"])

            bolsa = monedas - saldo_restante
            
            inventario.append(compra)
                
            while bolsa < 0 :
                print(f"Lo siento, no dispones de suficiente saldo {bolsa}, vuelve cuando hayas farmeado mejor..\n")
                break

            pregunta_3 = (input(str(f"\nDe acuerdo, tu saldo actual es de {bolsa} y tu inventario consta de {inventario}, ¿deseas comprar algo más?\n")))
            
            if pregunta_3.lower() not in afirmacion:  

                print("De acuerdo muchas gracias, vuelve cuando quieras")
                break
            
    elif pregunta_3.lower() not in afirmacion:  

        print("De acuerdo muchas gracias")
        
elif pregunta_2 not in afirmacion : 
    print("Otro indeciso.. Vuelve cuando quieras objetos a buen precio")


