#ANOTACION GENERAL: Pon los comentarios siempre arriba de la linea de código que quieres comentar


# Establezco el campeon
from typing import Dict, ValuesView


campeon="Lee sin"

# Establezo las monedas que tiene
monedas=500

# Establezco el inventario
inventario=["smite","potion"]

#ANOTACIÓN: DEJAMOS UN DICCIONARIO QUE LO TENÍAS COMENTADO Y VAMOS A QUITAR LA LISTA Y LOS VALORES QUE PONES MÁS ABAJO, IMPORTANTE PONERLE EN ESTE CASO MEJOR UN IDENTIFICADOR

objetos = {

    "a" : {
        "objeto" : "escudo de doran",
        "valor" : 200

    },

    "b":{
        "objeto" : "espada de doran",
        "valor" : 100

    },

    "c" : {
        "Objeto" : "espada de granizo",
        "valor" : 140

    },

    "d" : {
        "objeto" : "cuchilla de ascuas",
        "valor" : 350

    },

    "e" : {
        "objeto" : "preferencia",
        "valor" : 50

    },

    "f" : {
        "objeto" : "anillo de doran",
        "valor" : 350

    },

    "g" : {
        "objeto" : "sello oscuro",
        "valor" : 250

    },
}


#x=input(str("Qué deseas comprar\n"))


#values = objetos.values()

#for x in objetos :
print(objetos.keys())
#print(objetos["a"]["objeto"]["valor"])




#print(objetos.values[x])

#key=input(str(f"Hola {campeon}, ¿qué deseas comprar?\n")) 

#for i in range ((0,key)) :
    #print(objetos["a"]["objeto"])
    




#ANOTACIÓN: ¿QUÉ PASARÍA SI EN VEZ DE 7 OBJETOS TUVIERAS 500? NO NECESITAS TENER TODAS LAS OPCIONES YA PREDEFINIDAS, YA TIENES LOS DATOS EN EL DICCIONARIO Y TIENES UN VALOR Y UN MONEDERO. ¿QUÉ HARÍAS POR LÓGICA SI SABES LO QUE TIENES Y LO QUE TE VAS A GASTAR? PIENSA IGUAL A COMO LO HACIAS EN LOS PROBLEMAS DE MATEMÁTICAS DE PRIMARIAS


# Creo las respuestas de si esta seguro de comprar el objeto
#ANOTACIÓN: ESTO NO ES NECESARIO QUE VAYA EN UNA VARIABLE, SIMPLEMENTE LO PUEDES PONER EN LA CONDICIÓN

respuestas="si"

respuestas_2="no"




# Creo la primera pregunta para saber que desea comprar

#key=input(str(f"Hola {campeon}, ¿qué deseas comprar?\n"))

#for key in objetos :
 #   print(x["valor"])

# Lista de posibilidades acerca de las compras + un else si no se cumple nada

#ANOTACIÓN: ¿CÓMO ACCEDEMOS A LOS VALORES DE LOS DICCIONARIOS?


'''
if pregunta in objetos :

 

    if pregunta == objetos :

        print(f"Este {objetos}")

'''