fruitlijst = ["appel", "banaan", "perzik", "druif", "sinaasappel"]

fruit_invoer = input("Voer een fruitsoort in om te verwijderen: ")

if fruit_invoer in fruitlijst:
    fruitlijst.remove(fruit_invoer)
    print(f"{fruit_invoer} is verwijderd uit de lijst.")
else:
    print(f"{fruit_invoer} is niet gevonden in de lijst.")

print("De bijgewerkte lijst van fruitsoorten is:")
print(fruitlijst)
