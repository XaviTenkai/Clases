
cita_medico = 10 #declaramos variable y la inicializamos con valor 10
print(cita_medico) #imprimimos por consola la variable cita medico

cita_medico = 20 #reasignar valor de la variable
print(cita_medico)

#TIPOS VARIABLES
'''
    enteros (números) Numero de personas en una clase, Numero de FTDs, las veces que alguien tira a canasta, balones de oro que tiene Messi
    strings (cadenas de textos) Nombres de los empleados, nombres de campañas, el pais de origen de un empleado,
    booleanos (verdadero o falso) Un lead es test o no, Contraseña correcta o no, hechos reales (llueve o no llueve), 
    float (decimales) Porcentajes, coordenadas, coste por lead, grados centigrados, fechas, kilometros,
    
    dudas: matriculas, contraseña con distintos caracteres, lista de la compra, modelo de portatil
    
    objetos (por ahoar ni caso)
    listas (por ahora ni caso)
    tuplas (por ahora ni caso)
    diccionarios (por ahora ni caso)
'''

cita_medico = "10" #se pueden poner valores que sean de distinto tipo al inicialmente declarado. En este caso de entero a string
print(cita_medico)

'''
    LO QUE NO SE PUEDE DECLARAR COMO VARIABLE
    EXCEPCIONES:
    Primera: Nunca poner un número por delante: 2cita_medico
    Segunda: Guión intermedio: cita-medico
    Tercera: Espacios: cita medico
    
'''

'''
    CONVENCIONES
    Las variables en 
    snake case (palabras separadas con guión bajo)

'''
alero = 10
print(type(alero))
pivot = "Alex"
alero = "Marcos"
escolta = "Juan"
base = "Miguel"
entrenador = "Jaimito"

pivot, alero, escolta, base, entrenador = "Alex", "Marcos", "Juan", "Miguel", "Jaimito" #Forma abreviada de asignar multiples valores

print(type(alero)) #la función type nos dice el tipo de variable que estamos usando

print(alero)
pivot = alero =  escolta = base =  entrenador = "Neymar" #Asignar el mismo valor a múltiples variables

print(alero)

#FLOATS
cita_medico = 10.0 
print(cita_medico/3)

#BOOLEANOS
puede_pasar_a_la_discoteca = True


