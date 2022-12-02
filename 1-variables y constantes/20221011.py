
'''
cadena_corrupta = "airotsiH,6.7,aícraG nómaR"

cadena_volteada = cadena_corrupta[::-1]
print(cadena_volteada)

nombre = cadena_volteada[0:12]
print(nombre)

nota = cadena_volteada[13:16]
print(nota)

asignatura = cadena_volteada[17:25]
print(asignatura)


print(f"{nombre} ha sacado un {nota} en {asignatura}")



lista1 = [1, 12, 123]
lista2 = ["Bye", "Ciao", "Agur", "Adieu"]

lista1.append(1234)
lista1.append("Hola")
print(lista1)

lista2.append("Adios")
lista2.append(4321)
print(lista2)

lista3 = lista1[:(len(lista1)-1)]
print(lista3)

lista4 = lista2[1:(len(lista2)-1)]
print(lista4)

lista5 = lista3 + lista4
print(lista5)


nombre = input("introduce un nombre")
apellido = input("introduce un apellido")
edad = int(input("introduce tu edad"))
numero_magico = float(input("introduce tu numero de la suerte"))
cadena_final = nombre + " " + apellido + ": tu número de la suerte es el " + str(numero_magico)
print(cadena_final)



numero = int(input("Introduzca un número"))

while numero % 5 != 0 :
    numero = int(input("Introduzca un número"))

    
numero = ""

while numero not in range(1,10) :
    numero = int(input("Introduzca un número del 1 al 9\n"))

multiplos = (list(range(numero, 101, numero)))

print(multiplos)



matriz = [[8,7,0],
          [34,2,-1],
          [5, -5, 12]
]


# Completa el ejercicio aquí
for i, tabla in enumerate(matriz) :
    for j, numero in enumerate(tabla) :
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        else :
            matriz[i][j] = 1
        print(matriz[i][j], end=" ")
    print()


grupo = {"Miguel", "Blanca", "Mario", "Andrés"}

# Completa el ejercicio
usuario = ("Ana", "Ramón", "Marta", "Eric", "David")
for nombre in usuario :
    grupo.add(nombre)
print(grupo)

usuario2 = ("Mario", "Miguel", "Ramón")
for nombre in usuario2 :
    grupo.remove(nombre)
print(grupo)



animales = {"caballo":"", "vaca":""}

# completa el ejercicio
animales["perro"] = "dog"
animales["gato"] = "cat"
animales["rana"] = "frog"
print(animales)

animales["caballo"] = "Horse"
animales["vaca"] = "Cow"
print(animales)

del(animales["rana"])
del(animales["vaca"])
print(animales)


usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

administradores = {"Juan", "Marta"}

administradores.discard("Juan")

print(administradores)

administradores.add("Marcos")

print(administradores)

for usuario in usuarios :
    if usuario in administradores :
        print(f"{usuario} es un administrador")
    else :
        print(usuario)

caballero = {"vida" : 2, "ataque" : 2, "defensa" : 2, "alcance" : 2}
guerrero = {"vida" : 2, "ataque" : 2, "defensa" : 2, "alcance" : 2}
arquero = {"vida" : 2, "ataque" : 2, "defensa" : 2, "alcance" : 2}

caballero["vida"] = guerrero["vida"] * 2
caballero["defensa"] = guerrero["defensa"] * 2
guerrero["ataque"] = caballero["ataque"] * 2
guerrero["alcance"] = caballero["alcance"] * 2
arquero["vida"] = guerrero["vida"]
arquero["ataque"] = guerrero["ataque"]
arquero["defensa"] = guerrero["defensa"]/2
arquero["alcance"] = guerrero["alcance"] * 2

print(f"Caballero : {caballero}")
print(f"Guerrero : {guerrero}")
print(f"Arquero : {arquero}")


cartas = []
num_cartas = 1
for x in range(2) :
    cartas.append(input(f"Introduce tu {num_cartas}a carta\n"))
    num_cartas += 1
print(f"Tus mano es {cartas}")

print("{:>35}".format("Palabra")) # Alinear a la derecha

print("{:^35}".format("Palabra")) # Alinear al centro

print("{:.4}".format("Palabra")) # Truncamiento a 4 caracteres

print("{:>35.4}".format("Palabra")) # Alinear a la derecha + truncamiento


# Formateo de números enteros, rellenados con espacios
print("{:4d}". format(10))
print("{:4d}". format(100))
print("{:4d}". format(1000))


# Formateo de números enteros, rellenados con ceros
print("{:04d}". format(10))
print("{:04d}". format(100))
print("{:04d}". format(1000))


# Formateo de números flotantes, rellenados con espacios

print("{:.2f}".format(3.1415926))

# Alineación de números dlotantes, rellenados con espacios

print("{:7.2f}".format(3.1415926))
print("{:7.2f}".format(353.14))

Mirar módulo de f-strings del curso

# Funciones :
def tabla_del_5() :
    for numero in range(11):
        print(f"{numero} * 5 = {numero * 5}")

tabla_del_5()
#Las variables recogidas fuera de la función sí son susceptibles de entrar 
#dentro de la función, las variables definidas dentro de la función no pasaran a estar en el código de fuera

# En las funciones, después del return no se va a ejecutar nada más

def suma(a,b) :
    return a+b
r = suma(5,2)

print(r)

# Ejercicio funciones :
def par_o_impar(numero) :
    if numero %2 == 0 :
        print("Es un número par")
    else :
        print("Es un numero impar")

numero = (int(input("Dime un número\n")))

par_o_impar(numero)

#Las listas hacen referencia a la variable original en cambio las variables no. Ejemplo:


def doblar_valor(numero) :
    numero *= 2
n = 10
doblar_valor(n)
print(n)

def doblar_valores(numeros) :
    for i,n in enumerate(numeros) :
        numeros[i] *= 2
ns = [10, 50, 100]
doblar_valores(ns)
print(ns)

# Para asignar correctamente el valor a la variable deberemos hacerlo de la siguiente manera.

def doblar_valor(numero) :
    return numero * 2
n = 10
n = doblar_valor(n)
print(n)

# Argumentos indeterminados

def indeterminados_posicion(*args) :
    for arg in args :
        print(arg)
indeterminados_posicion(5, "Hola", [1,2,3,4,5])

def indeterminados_nombre(**kwargs) :
    for kwarg in kwargs :
        print(kwargs[kwarg])
indeterminados_nombre(n=5, c="Hola", l=[1,2,3,4,5]) 


def super_funcion(*args, **kwargs) :
    t = 0
    for arg in args :
        t+= arg
    print(f"El sumatorio indeterminado es {t}")
    for kwarg in kwargs :
        print(kwarg," ",kwargs[kwarg])
super_funcion(10,50,-1,1.56,nombre = "Hector", edad = 27)


# Funciones recursivas

import time


def cuenta_atras(num) :
    num -= 1
    if num > 0 :
        time.sleep(1)
        print(num)
        cuenta_atras(num)
    else :
        time.sleep(1)
        print("¡Boooooooooom!")
cuenta_atras(10)

def factorial(num) :
    if num > 1 :
        num = num * factorial(num - 1)
    return num

print(factorial(5))


def sumatorio(numero) :
    if numero > 0 :
        numero = numero + sumatorio(numero - 1)
    return numero

print(sumatorio(5))



def test(num) :
    return num, num*2, num*4
print(test(5))

#Ejercicio 103

def area_rectangulo(base, altura) :
    return base * altura
    
print(area_rectangulo(15, 10))

# Ejercicio 107

def recortar(numero, inferior, superior) :
    if numero < inferior :
        return inferior
    elif numero > superior :
        return superior
    else : 
        return numero
print(recortar(15, 0, 10))

# Ejercicio 108 

numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(numeros) :
    numeros.sort()
    pares = []
    impares = []
    for numero in numeros :
        if numero %2 == 0 :
            pares.append(numero)
        elif numero %2 != 0 :
            impares.append(numero)
    return pares, impares

pares, impares = (separar(numeros))
print(pares)
print(impares)


def numero(a,b) :
    try :
        return a/b
    except :
        return ("Lo siento no se puede dividir entre 0")

a = float(input("Introduce un número\n"))
b = float(input("Introduce otro número\n"))

print(numero(a,b))


try :
    n = float(input("Introduce un número\n"))
    print(5/n)
except TypeError :
    print("No se puede dividir el número por una cadena")
except ValueError :
    print("Debes introducir un número")
except ZeroDivisionError :
    print("No se puede dividir por 0")
except Exception as e :
    print(type(e).__name__)

# Revisar files con otro tipo de excepciones

# Clases y objetos

# Las clases son como los moldes para crear objetos

# Un método es la palabra que indica una función dentro de una clase


cards = ("4s", "5h")
class Player() :
    cards_showing = False
    
    def __init__(self) :
        print("Se acaba de crear un jugador")
    
    def cardsshowing(self) :
        self.cards_showing = True
    
    def show_down(self) :
        if p.cards_showing :
            print(cards)
        else :
            print("card, card")
        
p = Player()

p.cardsshowing()
p.show_down()

#127 Encapsulacion de atributos y metodos

class Ejemplo :
    __atributo_privado = print("Soy un atributo inalcanzable desde fuera")
    
    def __metodo_privado(self) :
        print("Soy un metodo inalcanzable desde fuera")
        
    def atributo_publico(self) :
        return self.__atributo_privado

e = Ejemplo()
e.__atributo_privado()
e.__metodo_privado()
e.atributo_publico()


import math

class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self) :
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self) :
        if self.x > 0 and self.y > 0 :
            print(f"El punto {self} pertenece al 1r cuadrante")
        elif self.x < 0 and self.y > 0 :
            print(f"El punto {self} pertenece al 2o cuadrante")
        elif self.x < 0 and self.y < 0 :
            print(f"El punto {self} pertenece al 3r cuadrante")
        elif self.x > 0 and self.y < 0 :
            print(f"El punto {self} pertenece al 4o cuadrante")
        else :
            print(f"El punto {self} se encuentra en el origen")
    
    def vector(self, p) :
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))
        
    def distancia(self, p) :
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print(f"La distancia entre los puntos {self} y {p} es {(d)}")

# Puntos del ejercicio: A(2,3), B(5,5), C(-3,-1), D(0,0)

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

#A.cuadrante()
#C.cuadrante()
#D.cuadrante()

#Punto.vector(A,B)
#Punto.vector(B,A)

#A.vector(B)
#B.vector(A)

#A.distancia(B)
#B.distancia(A)

#A.distancia(D)
#B.distancia(D)
#C.distancia(D)

class Rectangulo:
    def __init__(self, inicial = Punto(), final = Punto()) :
        self.inicial = inicial
        self.final = final
    
    def base(self) :
        self.base = abs(self.final.x - self.inicial.x)
        print(f"La base del rectangulo es {self.base}")
    
    def altura(self) :
        self.altura = abs(self.final.y - self.inicial.y)
        print(f"La altura del rectangulo es {self.altura}")
    
    def area(self) :
        self.base = abs(self.final.x - self.inicial.x)
        self.altura = abs(self.final.y - self.inicial.y)
        self.area = (self.base * self.altura)
        print(f"El area del rectangulo es {self.area}")
        
R = Rectangulo(A, B)
R.base()
R.altura()
R.area()


# Seccion 12 : Herencia de clases 

# La herencia : la capacidad de una clase de heredar atributos y métodos de otra,
# ademas de agregar de nuevos o modificar los heredados
# La relación de clases madre y clases hijas se conoce como Superclases y Subclases



class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion) :
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    
    def __str__(self) :
        return """\n
    REFERENCIA\t\t{}
    NOMBRE\t\t{}
    PVP\t\t\t{}
    DESCRIPCION\t\t{}
    """.format(self.referencia, self.nombre, self.pvp, self.descripcion)

class Adorno(Producto) :
    pass

a = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con árboles")

#print(a)

class Alimento(Producto) :
    
    def __init__(self, referencia, nombre, pvp, descripcion):
        super().__init__(referencia, nombre, pvp, descripcion)
    productor = ""
    distribuidor = ""
    
    def __str__(self) :
        return Producto.__str__(self) + """PRODUCTOR\t\t{}
    DISTRIBUIDOR\t{}
    """.format(self.productor, self.distribuidor)

al = Alimento(2035,"Botella de aceite de oliva", 5, "250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"

#print(al)

productos = [al, a]

#for p in productos :
    #print(p)
    
for p in productos :
    if (isinstance(p,Adorno)):
        print(p.referencia, p.nombre)
    elif(isinstance(p,Alimento)) :
        print(p.referencia, p.nombre, p.productor, p.distribuidor)

def rebajar_producto(p,rebaja) :
    #Devuelve un producto con una rebaja en porcentaje de su precio
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

al_rebajado = rebajar_producto(al,10)

print(al_rebajado)

import copy

copiar_ad = copy.copy(a)

copiar_ad.pvp = 25
print(a)
print(copiar_ad)

#Herencia múltiple 133
#polimorfia = propiedad de la herencia en que objetos de distintas subclases pueden responder una misma acción
#herencia múltiple = hace referencia a la posibilidad de que una sublclase herede varias super clases a la vez de manera que se pueden heredar multitud de atributos y métodos

class A:
    def __init__(self) :
        print("Soy de clase A")
    
    def a(self) :
        print("Este método lo heredo de A")

class B :
    def __init__(self) :
        print("Soy de clase B")
    
    def b(self) :
        print("Este método lo heredo de B")

class C(B,A) :
    def c(self) :
        print("Soy un método de clase C")

c = C()
# Siempre tiene en cuenta la clase de la que hereda más a la izquierda (linea 589)
print(c)

print(c.a())
print(c.b())
print(c.c())
'''











