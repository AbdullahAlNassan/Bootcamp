namenlijst = ["Alice", "Bob", "Charlie", "David", "Eva"]

ingevoerde_naam = input("Voer een naam in: ")

if ingevoerde_naam in namenlijst:
    namenlijst.remove(ingevoerde_naam)
    print(f"{ingevoerde_naam} is verwijderd.")
else:
    namenlijst.append(ingevoerde_naam)
    print(f"{ingevoerde_naam} is toegevoegd.")

print("De bijgewerkte lijst is:", namenlijst)
