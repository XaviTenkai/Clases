


pot_odd = int(input("¿Cuál es el bote?\n"))
rival_bet = int(input("¿Cuál es la apuesta del rival?\n"))

bet_over_the_pot = "{:.2%}".format(rival_bet/pot_odd)
print(f"\nEl porcentaje sobre el bote es del {bet_over_the_pot}")
odd_calculation = (pot_odd + rival_bet)/rival_bet
print(f"Las odds son de {int(odd_calculation)} : 1")

equity_calculation = "{:.2%}".format(rival_bet/(pot_odd + rival_bet + rival_bet))
print(f"La equity es de {equity_calculation}")
