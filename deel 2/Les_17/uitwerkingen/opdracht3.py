import random

def raad_het_getal():
    geheim_getal = random.randint(1, 5)
    geraden = False

    while not geraden:
        gebruiker_getal = int(input("Raad het getal tussen 1 en 5: "))
        
        if gebruiker_getal == geheim_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            geraden = True
        else:
            print("\033[91mJe hebt het getal niet goed geraden!\033[0m")

for _ in range(3):
    raad_het_getal()
