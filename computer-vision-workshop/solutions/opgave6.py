# Opgave 6

# Lav et lille spil
# Lav et program som printer tekst til jer, hvor i bagefter kan svarer med flere valgmuligheder. - Hav minimum to.
# Hav mindst to forskellige svar basseret på hvad du skriver. Eventuelt tilføj en mulighed hvis svaret ikke giver mening.

print("Du er i et rum, du kan gå til venstre eller højre, hvilken vej vil du gå?")


while True:
    answer = input()

    if answer == "højre":
        print("Du vandt")
        break
    elif answer == "venstre":
        print("Du tabte")
        break
    else:
        print("Det er ikke et svar, prøv at skrive det igen.")