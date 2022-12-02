#TIPOS VARIABLES
'''
    enteros (números) Numero de personas en una clase, Numero de FTDs, las veces que alguien tira a canasta, balones de oro que tiene Messi
    strings (cadenas de textos) Nombres de los empleados, nombres de campañas, el pais de origen de un empleado,
    booleanos (verdadero o falso) Un lead es test o no, Contraseña correcta o no, hechos reales (llueve o no llueve), 
    float (decimales) Porcentajes, coordenadas, coste por lead, grados centigrados, fechas, kilometros,
        
    objetos (por ahoar ni caso)
    listas (por ahora ni caso)
    tuplas (por ahora ni caso)
    diccionarios (por ahora ni caso)
    
    RESERVAS:
    Nombre de los empleados 
    Pais de origen de un empleado
    fechas
    
    DUDAS
    matriculas, contraseña con distintos caracteres, lista de la compra, modelo de portatil
'''

alumno = {  #clave : valor
               # futbolista: persona que juega al futbol
    "nombre" : "Jaimito",
    "primer_apellido" : "Messi",
    "edad": 8
}




escuela = {
    "jaimito" : {
        "primer_apellido" : "Messi",
        "edad": 12,
        "nota_media": 10
    },
    "pedrito" : {
        "primer_apellido" : "suarez",
        "edad": 11,
        "nota_media": 3
    },
       
}

print(escuela["pedrito"]["nota_media"])
