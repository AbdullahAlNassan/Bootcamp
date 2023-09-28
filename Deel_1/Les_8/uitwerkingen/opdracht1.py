cijfer = int(input("Voer het cijfer in: "))

cijfer_omschrijvingen = {
    10: "uitmuntend",
    9: "zeer goed",
    8: "goed",
    7: "ruim voldoende",
    6: "voldoende",
    5: "bijna voldoende",
    4: "onvoldoende",
    3: "gering",
    2: "slecht",
    1: "zeer slecht",
}

if cijfer in cijfer_omschrijvingen:
    omschrijving = cijfer_omschrijvingen[cijfer]
    print(f"Omschrijving voor cijfer {cijfer}: {omschrijving}")
else:
    print("Ongeldig cijfer. Voer een cijfer tussen 1 en 10 in.")
