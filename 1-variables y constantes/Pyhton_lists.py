#Python Lists 1 Ejercicio

from typing import List


print("EX1")

mylist_1=('Apple', 'Samsung', 'Sony', 'Blackberry')
print(mylist_1)
print(len(mylist_1))
mylist_2=(2, 4)
mylist_3=(True, False, False, True)
print(mylist_1, mylist_2, mylist_3)
print(len(mylist_1))
print(len(mylist_2))
print(len(mylist_3))
mylist_4=('Samsung', True, 44)
print(mylist_4)
print(type(mylist_1))
print(type(mylist_2))
print(type(mylist_3))
print(type(mylist_4))

mylist_5=list(("Apple", "Samsung", "Sony", "Blackberry"))
print(mylist_5)
print(type(mylist_5))
mylist_5=list(("Apple", 64, "Sony", "Blackberry"))
print(mylist_5)
mylist_1=('Apple', 'Samsung', 'Sony', '28')
print(mylist_1)
#Mas abajo pone que las Tuples no se pueden cambiar, sinembargo para la mylist_1 si que he podido hacerlo. 
#La mylist_5 al ser del tipo list entiendo que es correcto que se modifique

'''
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
    
'''
#Tuples 2 Ejercicio

print("EX2")

mytuple_1=("Lenovo", "Mac", "Acer", "Omen")
print(mytuple_1)
mytuple_1=("Lenovo", "Mac", "Acer", "Omen", "Lenovo", "Mac", "Acer", "Omen")
print(mytuple_1)
print(type(mytuple_1))
not_a_tuple=("Lenovo")
mytuple_3=("Lenovo",)
print(type(not_a_tuple))
print(type(mytuple_3))
mytuple_4=tuple(("HP"))
print(type(mytuple_4))
mytuple_5=tuple((False, True, True, False))
print(type(mytuple_5))
not_a_tuple_2=list((False, True, True, False))
print(type(not_a_tuple_2))
print(mytuple_5)
print(not_a_tuple_2)
#¿En qué momento me interesa más hacer una tuple o una list? Imagino que la list es por si quiero modificar cosas dentro de esa list
# a lo largo del código y la tuple es para hacerlo estático y que siempre me devuelva los mismos valores (aunque mas arriba he modificado una tuple)

#Conditions 3 Ejercicio

print("EX3")

a=5
b=8
#a==b
#a=!b
#a<=b
#a>=b

if b>=a : 
    print("b is equal or greater than a")
else :
    print("a is greater than b")

c=a+3

if c>b : 
    print("c is greater than b")
elif c==b :
    print ("b equals to c")
else : 
    print("b is greater than c")
    
d=c * 2   
    
if d>b : 
    print("d is greater than b")
elif d==b :
    print ("b equals to d")
else : 
    print("b is greater than d")

#print(a,b,c,d)

print ("Equals") if b+c == d else print("Not equals")

e=a*5

print ("b&c") if b+c > e else print("Equals") if b+c==e else print ("e")

#print(a,b,c,d,e)

if e>d and d>c :
    print("Both coniditions are true")
    
if e>d and d==c*2 and d!=a and b+c==d:
    print("All coniditions are true")
    
if e<d or d==c*2:
    print("At least 1 is true")
    
if e>a+b:
    print("Above a+b")
    if e>d:
        print("Also above d")
    else:
        print("Not above d")

f=14
if f>a+b:
    print("Above a+b")
    if f>d:
        print("Also above d")
    else:
        print("Not above d")
#Me gusta porque no es un condicionante de una cosa u otra

if f>a+b:
    pass

if e>a+b:
    print("Above a+b")
    if e>d:
        pass
    else:
        print("Not above d")

g=14
print("Z")
if g>a+b:
    pass
    if g>0:
        print("Also above d")
    if g>1:
        print("g Equals e")
    else:
        print("Not above d")
    
print(a,b,c,d,e,f)

print("Y")
if g>a+b:
    print("g is greater than a+b")
    if g>d:
        print("Also above d")
    else:
        print("Not above d")
        
#¿Me guarda el pass que he hecho mas arriba? Despues de print Z, en print Y no me aparece nada. Mas abajo si cambio el g>a+b por 
# g<a+b si que me lo reconoce

print("n")
if g<a+b:
    print("g is greater than a+b")
elif g>d:
        print("Also above d")
elif g!=e:
        print("g is different from e")
else:
        print("Not above d")
        
#Syntax 4 Ejercicio

print("EX4")

print("Bienvenidos a League of Draven")
#Sorry por la frikada

#Este apartado no tenia mucho mas y es muy corto, cosas que ya he hecho en anteriores (Identation, variables)

#Ejercicio Aitor: ¿podemos encontrar un identificador de campaña ficticio en una lista?

print("Ejercicio Aitor")

#2b8a7435-3bde-4a06-a87c-ab41ebd9966d - 36

a="2b8a7435-3bde-4a06-a87c-ab41ebd9966d"

x= (len(a))
    
if x==36: 
    print("Standard Length")
else:
    print("Non standard Length")
    
#Sabemos que tiene una longitud "Standard", podria ser un factor para determinar si es o no un identificado ficticio
    
print(type(a))

r=list(("2b8a7435-3bde-4a06-a87c-ab41ebd9966d","d79fefb3-6abc-44c3-b7bd-d5ddce142a4f", "4b74c187-d5a1-47d3-b056-490c581d458c", "8dcec700-0add-4272-8ccc-cb5e18e7a9b5"))

s=len(r)

print(type(r))

if s==36: 
    print("Standard Length")
else:
    print("Non standard Length")
    
print(len(r))
    
#Queria ver si tambien servia la funcion de len para una lista, pero veo que no. Me cuenta el numero de valores, no los caracteres de cada valor.