

def objeto_que_se_quiere_comprar():
    from valores import objetos
    print("\nLo siento no te he entendido, ¿puedes volver a repetirlo?")
    compra = input(str("\n¿Qué deseas comprar?\n"))
    if compra.lower in objetos :
        return compra   

def mostrar_objetos():
    import pprint
    from valores import objetos
    pprint.pprint(objetos)
    
def mostrar_informacion_compra(compra):
    from valores import objetos
    print(f"\nEl valor de {compra.lower()} es de:",end=" ")
    print (objetos[compra.lower()]["valor"])
    
def mostrar_precio(compra):
    from valores import objetos
    return int(objetos[compra.lower()]["valor"])
    
def calcular_saldo(monedas, precio):
    return monedas-precio
