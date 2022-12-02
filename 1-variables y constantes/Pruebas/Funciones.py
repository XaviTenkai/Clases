


def reparto_cartas() : 
    import random
    #from Class import Mano1
    from Valores import card_deck, card_deck1, card_deck2

    numero1 = ""
    
    while numero1 not in card_deck : 
        numero1 = random.choice(card_deck1) + random.choice(card_deck2)
        if numero1 in card_deck :
            break
        card_deck.remove(numero1)
    
    #palo1 = ""
    '''
    while palo1 not in card_deck : 
        palo1 = random.choice(card_deck1) + random.choice(card_deck2)
        if palo1 in card_deck :
            break
        card_deck.remove(palo1)
'''
    p1 = (numero1)
    p1.myfunc()
    
    print(numero1)

