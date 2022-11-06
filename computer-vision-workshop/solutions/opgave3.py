# Opgave 3

# Lav en if statement.
# Gem et tal under navnet A, og check om A er større ind 100. Hvis A er større ind 100 print "Stor", hvis
# A er mindre ind 100 print lille.

A = 150

if A > 100:
    print("Stor")
else:
    print("Lille")


# Mere complicerede løsning

if A > 100:
    print("Stor")
elif A < 100 and A > 50:
    print("Mellem")
else:
    print("Lille")
