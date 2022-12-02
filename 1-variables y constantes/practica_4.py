#variable=input("Introduzca un nombre\n")
#print(variable)

'''
    Usuario tiene 500 monedas de oro y quiere comprar los elementos que quiere.
        - Definir usuario y establecer que tiene 500 monedas de oro
            - Variable de campeon
            - Variable de monedas de oro
    La tienda tiene prefijadods sus propios productos con sus precios
        - Definir objetos de la tienda y sus precios
            -Lista de objetos
    El usuario tiene su propio inventario
    
    EJERCICIO:
    Pedir al usuario que haga una compra de lo que desee y al final del proceso se muestre su saldo actual junto al elemento que ha
        - Utilizar el input a modo pregunta para preguntar al usuario que desea
        - Una vez introducido el objeto, hacer la resta de las monedas - el/los producto/s que ha comprado
    comprado dentro de su inventario 
    
    PROCEDIMIENTO PARA REALIZAR EL EJERCICIO
    1- Desgranar el enunciado en partes pequeñas
    2- Definir con qué tipo de elementos se v a atrabajar en cada parte
    3- Si se puede deshilar más de deshilar (respecto al punto 1)
    4- Diseñar algoritmo a modo de comentarios de texto en el código como estás viendo esto ahora 
    Punto  1, 2, 3, 4  y 5 (70% del tiempo)
    5- Crear microtareas 
    6- Implementar el código (20% del total del tiempo)
    7- Probar (10%)
    
    ANTE UNA DUDA:
    -Primero buscar en San Google priorizando Stackoverflow o W3School si es algo de sintaxis
    -Si no lo he encontrado contactar  Aitor y me pones lo que has buscado
    -Volver a interalo
    
    SOBRETODO:
    -Paciencia y la frustración es tu mejor compañera de trabajo, hazte amigo de ella ;-)
    
'''

campeon="Lee sin" 
# Establezco el campeon

monedas=500
#Establezo las monedas que tiene

inventario=["smite","potion"]

objetos=["escudo de doran", "espada de doran", "espada de granizo", "cuchilla de ascuas", "preferencia", "anillo de doran", "sello oscuro"]
# Creo la lista de los objetos

'''objetos = {
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
    }
        
}
'''
# Prueba que no ha salido bien

# Creo los valores
a=200
b=100
c=140
d=350
e=50
f=350
g=250

# Creo las restas de las monedas menos el valor del objeto
h=monedas-a
i=monedas-b
j=monedas-c
k=monedas-d
l=monedas-e
m=monedas-f
n=monedas-g

# Creo las respuestas de si esta seguro de comprar el objeto
respuestas="si"
respuestas_2="no"

# Creo la primera pregunta para saber que desea comprar
pregunta=input(str(f"Hola {campeon}, ¿qué deseas comprar?\n"))

# Lista de posibilidades acerca de las compras + un else si no se cumple nada
if pregunta in objetos : 

    if pregunta == "escudo de doran" :
        print(f"Este objeto cuesta {a}")
    elif pregunta == "espada de doran" :
        print(f"Este objeto cuesta {b}")
    elif pregunta == "espada de granizo" :
        print(f"Este objeto cuesta {c}")
    elif pregunta == "cuchilla de ascuas" :
        print(f"Este objeto cuesta {d}")
    elif pregunta == "preferencia" :
        print(f"Este objeto cuesta {e}")
    elif pregunta == "anillo de doran" :
        print(f"Este objeto cuesta {f}")
    elif pregunta == "sello oscuro" :
        print(f"Este objeto cuesta {g}")

# Segunda pregunta de si esta seguro de si desea comprarlo con un else por si dice que no
    pregunta_2=input(str("¿seguro que quieres comprarlo? ¿si o no?\n"))

    if pregunta_2==respuestas :

                if pregunta == "escudo de doran" :
                    print((f"De acuerdo, gracias por tu compra te quedan {h} monedas"))
                elif pregunta == "espada de doran" :
                    print((f"De acuerdo, gracias por tu compra te quedan {i} monedas"))
                elif pregunta == "espada de granizo" :
                    print((f"De acuerdo, gracias por tu compra te quedan {j} monedas"))
                elif pregunta == "cuchilla de ascuas" :
                    print((f"De acuerdo, gracias por tu compra te quedan {k} monedas"))
                elif pregunta == "preferencia" :
                    print((f"De acuerdo, gracias por tu compra te quedan {l} monedas"))
                elif pregunta == "anillo de doran" :
                    print((f"De acuerdo, gracias por tu compra te quedan {m} monedas"))
                elif pregunta == "sello oscuro" :
                    print((f"De acuerdo, gracias por tu compra te quedan {n} monedas"))
# Le indico el saldo restante
                inventario.append(pregunta)
                print(f"Tu inventario actual es {inventario}")

    elif pregunta_2==respuestas_2:

                print("De acuerdo, gracias igualmente")

    else :

                print("Lo siento, no te he entendido, vuelve cuando quieras")

else:

    print("No dispongo de ese objeto, vuelve cuando quieras") 
