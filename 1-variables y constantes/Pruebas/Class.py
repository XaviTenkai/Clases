


class Mano :

    def __init__(self, numero1, palo1) :
        
        self.numero1 = numero1
        self.palo1 = palo1

    def myfunc(self) : 
        print("Tu mano es " + self.numero1  + " de " + self.palo1)
    
mano1 = Mano("10", "picas")
mano2 = Mano("4", "corazones")

mano1.myfunc()
mano2.myfunc()
    

            






