'''
Primero las estructuras de código (variables, listas, tuplas, diccionarios...)

TAREA: Poner todo lo que se pueda repetir o ser suceptible de repetir con alguna pequeña modificación en funciones

TAREA 2: Poner el menú de una forma en la que si el usuario teclear salir salga de la aplicación y si no, una vez ejecute la acción que quiera ejecutar

retornarlo de nuevo al menú principal.

'''


# Creando la primera pregunta para saber qué desea comprar

from valores import campeon
from funciones import objeto_que_se_quiere_comprar, mostrar_objetos, mostrar_informacion_compra, calcular_saldo

print(f"\nHola {campeon}, dispongo de los siguientes objetos: ", end="" )




mostrar_objetos()

compra = ""
while True:
    compra = objeto_que_se_quiere_comprar
    if compra !=None:
        
        break

    

print(mostrar_informacion_compra(compra))


afirmacion = ["si"]

pregunta_2 = input(str("\n¿Estás seguro que deseas comprarlo?\n"))


#bolsa = monedas - saldo_restante


monedas = calcular_saldo(monedas, precio)

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


