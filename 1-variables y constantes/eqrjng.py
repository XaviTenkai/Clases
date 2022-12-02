
class Mano1 : 
    def __init__(self, numero1, palo1, numero2, palo2) :
        
        self.numero1 = numero1
        self.palo1 = palo1
        self.numero2 = numero2
        self.palo2 = palo2
        

    def myfunc(self) : 
        print("Tu mano es " + self.numero1 + self.palo1 + " and " + self.numero2 + self.palo2)


p1 = Mano1("10", "h", "8", "c")


#p1.numero1

p1.myfunc()















