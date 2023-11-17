import random

def is_geldig_invoer(waarde, lijst):
    return waarde in lijst

def raad_het_getal():
    geheim_getal = random.randint(1, 5)
    toegestane_range = list(range(1, 6))
    geraden = False

    while not geraden:
        gebruiker_getal = int(input("Raad het getal tussen 1 en 5: "))

        while not is_geldig_invoer(gebruiker_getal, toegestane_range):
            print("Ongeldige invoer. Voer een getal tussen 1 en 5 in.")
            gebruiker_getal = int(input("Raad het getal tussen 1 en 5: "))

        if gebruiker_getal == geheim_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            geraden = True
        else:
            print("\033[91mJe hebt het getal niet goed geraden!\033[0m")

aantal_ronden = 0
aantal_fouten = 0

while True:
    aantal_ronden += 1
    aantal_fouten += raad_het_getal()

    nog_een_ronde = input("Wil je nog een ronde spelen? (ja/nee): ").lower()

    while not is_geldig_invoer(nog_een_ronde, ["ja", "nee"]):
        print("Ongeldige invoer. Voer 'ja' of 'nee' in.")
        nog_een_ronde = input("Wil je nog een ronde spelen? (ja/nee): ").lower()

    if nog_een_ronde != "ja":
        break

print(f"\nJe hebt {aantal_ronden} ronden gespeeld.")
print(f"Je hebt {aantal_fouten} keer fout geraden.")
