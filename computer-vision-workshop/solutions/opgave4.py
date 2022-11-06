# Opgave 4

# Lav et "for loop" og et "while loop".
# Ved brug af to forskellige løkker få konsolen til at printe "Hello" 10 gange

for i in range(10):
    print("Hello")

k = 0
while k < 10:
    print("Hello")
    k = k + 1


# While kan også skrives sådan her
k = 0
while True:
    print("Hello")

    k = k + 1
    if k > 10:
        break