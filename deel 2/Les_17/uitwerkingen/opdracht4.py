import random

def raad_het_getal():
    geheim_getal = random.randint(1, 5)
    geraden = False
    fouten = 0

    while not geraden:
        gebruiker_getal = int(input("Raad het getal tussen 1 en 5: "))
        
        if gebruiker_getal == geheim_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            geraden = True
        else:
            print("\033[91mJe hebt het getal niet goed geraden!\033[0m")
            fouten += 1

    return fouten

aantal_ronden = 0
aantal_fouten = 0

while True:
    aantal_ronden += 1
    aantal_fouten += raad_het_getal()

    nog_een_ronde = input("Wil je nog een ronde spelen? (ja/nee): ").lower()
    if nog_een_ronde != "ja":
        break

print(f"\nJe hebt {aantal_ronden} ronden gespeeld.")
print(f"Je hebt {aantal_fouten} keer fout geraden.")
