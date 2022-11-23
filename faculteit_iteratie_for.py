def fac(n):
    uitkomst = 1
    for i in range(1, n + 1):
        uitkomst = uitkomst * i
    return uitkomst


getal = int(input("Geef het getal in waarvan je de faculteit wil berekenen."))
print("De faculteit van ", getal, "is ", fac(getal))
