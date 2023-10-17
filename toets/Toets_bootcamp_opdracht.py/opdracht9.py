while True:
    invoer = input("Voer een getal tussen 0 en 10 in: ")
    if invoer.isdigit():
        getal = int(invoer)
        if 0 <= getal <= 10:
            print(f"Je hebt het juiste getal ingevoerd: {getal}")
            break
    print("Foutmelding: Voer een geldig getal tussen 0 en 10 in.")