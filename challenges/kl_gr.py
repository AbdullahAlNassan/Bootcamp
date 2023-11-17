largest_number = float('-inf')
smallest_number = float('inf')
divisible_by_3_count = 0

for _ in range(10):
    try:
        number = float(input("Voer een getal in: "))
        
        largest_number = max(largest_number, number)
        smallest_number = min(smallest_number, number)

        if number % 3 == 0:
            divisible_by_3_count += 1

    except ValueError:
        print("Ongeldige invoer. Voer een getal in.")

print(f"Het grootste getal is: {largest_number}")
print(f"Het kleinste getal is: {smallest_number}")
print(f"Het aantal getallen deelbaar door 3 (zonder rest) is: {divisible_by_3_count}")
