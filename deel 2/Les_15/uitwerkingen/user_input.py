from user_input import get_integer, get_float, get_string, get_letter

leeftijd = get_integer("Voer je leeftijd in: ")
print(f"Je leeftijd is: {leeftijd}")

bedrag = get_float("Voer het bedrag in: ")
print(f"Het bedrag is: {bedrag}")

naam = get_string("Voer je naam in: ")
print(f"Je naam is: {naam}")

letter = get_letter("Voer een letter in: ")
print(f"De ingevoerde letter is: {letter}")
