def grade_conversion(score):
    if 0 <= score <= 10:
        if 8.5 <= score <= 10:
            return "A"
        elif 7.5 <= score < 8.5:
            return "B"
        elif 6.5 <= score < 7.5:
            return "C"
        elif 5.5 <= score < 6.5:
            return "D"
        else:
            return "F"
    else:
        raise ValueError("Ongeldig cijfer. Voer een cijfer in tussen 0 en 10 (inclusief).")

try:
    user_score = float(input("Voer het cijfer in: "))
    letter_grade = grade_conversion(user_score)
    print(f"Het cijfer {user_score} komt overeen met de lettergrade: {letter_grade}")
except ValueError as e:
    print(f"Fout: {e}")
