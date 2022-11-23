def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

getal = int(input("Geef het getal in waarvan je de faculteit wil berekenen:"))
print("De faculteit van", getal, "is",fact(getal))