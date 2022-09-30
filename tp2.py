


import random

n = random.randint(0,100)
appreciation = "?"
nbr = 0
print("J'ai choisi un nombre entre 0 et 100 a vous de le deviner")
while True:
    var = input("Entrez un nombre:")
    var = int(var)
    if var < n :
        nbr = +1
        appreciation = "Mauvais reponse, le nombre est plus grande que:"
        print(appreciation, var)

    else :
        nbr = +1
        appreciation = "Mauvais reponse, le nombre est plus petit que:"
        print(appreciation, var)
    if var == n:
        appreciation = "Bravo le nombre etait:"
        print(appreciation, var, "Nombre de tentative:", nbr)
        break