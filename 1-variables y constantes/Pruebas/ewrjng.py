from collections import Counter

numbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suits = ["♠","♢","♣","♡"]
Standard_deck = []

for number in numbers :
    for suit in suits :
        #print(number, suit)
        card = str(number) + suit
        Standard_deck.append(card)

test_hands = ["J♠", "J♢","8♠", "10♢", "A♠"]

for card in test_hands :
    Standard_deck.remove(card)

player_hand = ["8♢", "J♣"]

for card in player_hand :
    Standard_deck.remove(card)

table_values = []
table_suits = []
#player_hand_values = []
#player_hand_suits = []

def suit(card) :
    return(card[-1])

def value(card) :
    if (card[0] == "A") :
        return 14
    if (card[0] == "J") :
        return 11
    if (card[0] == "Q") :
        return 12
    if (card[0] == "K") :
        return 13
    return(int(card[0:-1]))

for card in player_hand :

    table_values.append(value(card))

for card in player_hand :

    table_suits.append(suit(card))

for card in test_hands :

    table_values.append(value(card))

for card in test_hands :

    table_suits.append(suit(card))

print(table_values)
print(table_suits)

conteo = Counter(table_values)

resultado = {}
for repetido in table_values:  
    valor_numeros=conteo[repetido]
    if valor_numeros != 1:
        resultado[repetido] = valor_numeros
print(resultado)
    
conteo = Counter(table_suits)

resultado = {}
for repetido in table_suits:  
    valor_suits=conteo[repetido]
    if valor_suits != 1:
        resultado[repetido] = valor_suits
print(resultado)

print(Standard_deck)

