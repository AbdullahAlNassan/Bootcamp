MAX = 20
getal = int(input("Voer een getal in"))

if getal > MAX:
    print(f"Het getal is groter dan {MAX}")
elif getal < MAX:
    print(f"Het getal is kleiner dan {MAX}")
else:
    print(f"Het getal is gelijk aan {MAX}")