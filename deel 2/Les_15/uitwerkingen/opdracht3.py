# user_input.py

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Voer een geldig geheel getal in.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Voer een geldig decimaal getal in.")

def get_string(prompt):
    return input(prompt)

def get_letter(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.upper()
        else:
            print("Ongeldige invoer. Voer precies één letter in.")
