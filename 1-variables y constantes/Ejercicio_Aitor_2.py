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

monedas =  0
saldo_restante = 0
bolsa = 0

# Creando inventario del campeon
inventario=["smite","potion"]

# Creando la primera pregunta para saber qué desea comprar

print(f"\nHola {campeon}, dispongo de los siguientes objetos: ", end="" )

print(str(objetos.keys()).replace("{","").replace("}", "").replace("'", "").replace("[","").replace("]","").replace("dict_keys","").replace("(","").replace(")",""))


def loop() :
    
    compra = input(str("\n¿Qué deseas comprar?\n"))
    
    while compra.lower() not in objetos :
        print("\nLo siento no te he entendido, ¿puedes volver a repetirlo?")
        compra = input(str("\n¿Qué deseas comprar?\n"))
        if compra.lower in objetos : 
            break

    print(f"\nEl valor de {compra.lower()} es de:",end=" ")
    print (objetos[compra.lower()]["valor"]) 
    
    saldo_restante = int(objetos[compra.lower()]["valor"])
    
    afirmacion = ["si"]

    pregunta_2 = input(str("\n¿Estás seguro que deseas comprarlo?\n"))
    monedas = 500
    bolsa = monedas - saldo_restante
    continue

    def loop_2() : 
    
        if pregunta_2.lower() in afirmacion :
            
            while bolsa >= 0 :
            
                pregunta_3 = (input(str(f"\nDe acuerdo, tu saldo actual es de {bolsa}, ¿deseas comprar algo más?\n")))
                bolsa = monedas - saldo_restante
            
                if pregunta_3.lower() in afirmacion : 
                    monedas = bolsa
                    loop()
                
                if pregunta_3.lower() not in afirmacion:  
                        print("De acuerdo, ¡hasta la próxima!")
                
                if bolsa < 0 :
                    break
                
            
        elif pregunta_2.lower() not in afirmacion:  
                print("De acuerdo muchas gracias")
                
loop()
                













'''
# Creando la frase para los valores del diccionario + segunda pregunta de si esta seguro
if compra.lower() in objetos :

    print(f"\nSu valor es de: ", end="") 

    print(objetos[compra.lower()]["valor"], end=" ")
    print("\n")

    #print(objetos.get(x)) - Prueba que no ha salido bien

    y = input(str("¿Estás seguro que deseas comprar este objeto? ¿Si o no?\n"))

# Creando las posibilidades dentro de la pregunta

    if y.lower() == "si" :

        r = (objetos[x.lower()]["valor"])

        def resta(monedas, r):
            resultado = monedas - r

# Añadiendo al inventario el objeto que ha comprado 
            inventario.append(x.lower())
        
            print(f"\nGracias por tu compra, tu saldo ahora mismo es de: {resultado} y actualmente tu inventario consta de {inventario}\n" )

# Preguntando si quiere comprar algo mas
        t = input(str(f"¿Deseas comprar algo más {campeon}? ¿Si o no?\n"))

# Creando las posibilidades de respuesta: si, no o else        
        if t.lower()== "si" :
            v = input("\nDe acuerdo, ¿qué deseas comprar?\n")

# Si la respuesta es si, hago algo parecido a lo que he hecho anteriormente, añadiendo la posibilidad de que el nuevo objeto que compre supere su saldo actual           
            if v.lower() in objetos : 
                print("\nSu valor es de: ", end="")
                print(objetos[v.lower()]["valor"], end="")
                q = input(f", ¿quieres proceder con la compra?\n")
                if q.lower() == "si" :
                    l = (objetos[v.lower()]["valor"])
                    p = resultado - l
                    if p >= 0 :
# Si no supera el saldo actual le informo de su nuevo saldo y de su inventario actualizado
                        inventario.append(v.lower())
                        print(f"\nMuchas gracias, tu saldo ahora mismo es de: {p} y actualmente tu inventario consta de {inventario}")
# Si lo supera le digo que se vaya a farmear mejor
                    elif p < 0 :
                        print (f"\nLo siento no dispones de suficiente saldo ({z}) para comprar este objeto({l}), vuelve cuando hayas farmeado mejor")
# No he añadido la opcion de que no pueda comprar el mismo objeto porque en el LOL si que se puede tener el mismo objeto mas de una vez
                elif q.lower() == "no":
                    print("\nOk, nos vemos")
                else : 
                    print("\nNo te he entendido, pero muchas gracias por tu visita")
            else :
                print("\nLo siento, no dispongo ahora mismo de este objeto, ¡Vuelve pronto!")   
                
                      
            
        elif t.lower() == "no" :
            print("\nDe acuerdo, ¡Hasta pronto!")
        
        else :
            print("\nLo siento, no te he entendido ¡Adiós!")


   

    elif y.lower() == "no" :

        print("\nDe acuerdo, hasta pronto")

   

    else :

        print("\nLo siento, no te he entendido")

       

 

else :

    print("\nLo siento, no dispongo de este objeto")

 

# Pruebas

#for x in objetos :

    #print(x)

 

#key = objetos.keys()

 

#for x in objetos :
    #print(objetos["x"])
'''
