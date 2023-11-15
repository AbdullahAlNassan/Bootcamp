kleuren = ("rood", "blauw", "groen", "geel", "paars")

naam = input("Wat is jouw naam? ")

favoriete_kleur = input("Wat is jouw favoriete kleur? ")

if favoriete_kleur.lower() in kleuren:
    print(f"Hallo {naam}, jouw favoriete kleur, {favoriete_kleur}, is geweldig!")
else:
    print("Deze kleur is niet zo geweldig!")
