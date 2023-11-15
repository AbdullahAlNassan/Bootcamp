aantal_studenten = int(input("Hoeveel studenten zijn er in jouw klas? "))

collegegeld_per_jaar = 1115

totaal_collegegeld = aantal_studenten * collegegeld_per_jaar

print(f"Het totaal bedrag aan collegegeld betaald door alle studenten is: €{totaal_collegegeld}")

bedrag_appels = 3.40
bedrag_druiven = 2.45
bedrag_bananen = 1.95

btw_tarief_fruit = 0.09

btw_appels = bedrag_appels * btw_tarief_fruit
btw_druiven = bedrag_druiven * btw_tarief_fruit
btw_bananen = bedrag_bananen * btw_tarief_fruit

# Totaal BTW
totaal_btw = btw_appels + btw_druiven + btw_bananen

print(f"De BTW voor al het fruit in de fruitmand is: €{totaal_btw}")
