
'''
for x in range(8) :
    print(x)

for y in range(5,10) : 
    print(y)
    
'''    
    
import random
    
card_deck = ["2h","3h","4h","5h","6h","7h","8h","9H","10h","Jh","Qh","Kh","Ah",
             "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
             "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
             "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad"]


#player_name_1 = input("¿Cómo te llamas jugador número 1?\n")

player_name_1 = "Negreanu"
player_name_2 = "Doyle Brunson"
player_name_3 = "Phil Helmuth"
player_name_4 = "Adrian Mateos"

random_card_1 = random.choice(card_deck)
card_deck.remove(random_card_1)

random_card_2 = random.choice(card_deck)
card_deck.remove(random_card_2)

random_card_3 = random.choice(card_deck)
card_deck.remove(random_card_3)

random_card_4 = random.choice(card_deck)
card_deck.remove(random_card_4)

random_card_5 = random.choice(card_deck)
card_deck.remove(random_card_5)

random_card_6 = random.choice(card_deck)
card_deck.remove(random_card_6)

random_card_7 = random.choice(card_deck)
card_deck.remove(random_card_7)

random_card_8 = random.choice(card_deck)
card_deck.remove(random_card_8)

#print(card_deck)

player1 = random_card_1, random_card_5
player2 = random_card_2, random_card_6
player3 = random_card_3, random_card_7
player4 = random_card_4, random_card_8

print(f"{player_name_1} :", end=" ")
print(str(player1).replace("(","").replace(")","").replace("'","").replace(",",""))

print(f"{player_name_2} :", end=" ")
print(str(player2).replace("(","").replace(")","").replace("'","").replace(",",""))

print(f"{player_name_3} :", end=" ")
print(str(player3).replace("(","").replace(")","").replace("'","").replace(",",""))

print(f"{player_name_4} :", end=" ")
print(str(player4).replace("(","").replace(")","").replace("'","").replace(",",""))

burn_card_1 = random.choice(card_deck)
card_deck.remove(burn_card_1)

flop_1 = random.choice(card_deck) 
card_deck.remove(flop_1)
flop_2 = random.choice(card_deck)
card_deck.remove(flop_2)
flop_3 = random.choice(card_deck)
card_deck.remove(flop_3)

flop = flop_1, flop_2, flop_3

print(str(flop).replace("(","").replace(")","").replace("'","").replace(",",""), end=" ")

burn_card_2 = random.choice(card_deck)
card_deck.remove(burn_card_2)

turn = random.choice(card_deck)
card_deck.remove(turn)

print(turn, end=" ")

river = random.choice(card_deck)
card_deck.remove(river)

print(river)

player1_cards_number = random_card_1.__getitem__(0), random_card_5.__getitem__(0)

print(player1_cards_number)

#print(card_deck)


