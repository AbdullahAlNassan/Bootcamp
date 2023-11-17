try:
num = int(input("Voer een getal in: "))
    
    if num >= 0:
        for i in range(num + 1):
            print(num - i)
    else:
        for i in range(abs(num) + 1):
            print(num + i)

except ValueError:
    print("Ongeldige invoer. Voer een geheel getal in.")