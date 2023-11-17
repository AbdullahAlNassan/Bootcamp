
aantal_studenten = int(input("Hoeveel studenten zijn er in jouw klas? "))
collegegeld_per_jaar = 1115 

kosten_appels = 3.40
kosten_druiven = 2.45
kosten_bananen = 1.95

btw_tarief_fruit = 0.09  

totaal_collegegeld = aantal_studenten * collegegeld_per_jaar


btw_appels = kosten_appels * btw_tarief_fruit
btw_druiven = kosten_druiven * btw_tarief_fruit
btw_bananen = kosten_bananen * btw_tarief_fruit


totaal_btw_fruit = btw_appels + btw_druiven + btw_bananen


print(f"Het totaal bedrag aan collegegeld betaald door alle studenten is: €{totaal_collegegeld}")
print(f"De BTW voor al het fruit in de fruitmand is: €{totaal_btw_fruit}")

