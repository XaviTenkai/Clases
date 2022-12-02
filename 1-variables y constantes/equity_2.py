
player_hand = [2,5]

number_of_cards_preflop = 52
players_cards = 2
flop = 4
turn = 2
river = 2

number_of_players = int(input("¿Número de jugadores?\n"))



number_of_cards_flop = number_of_cards_preflop - (number_of_players * players_cards) - flop

outs_flop = 2 * 3 / number_of_cards_flop

print(outs_flop)
