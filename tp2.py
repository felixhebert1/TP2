


import random
nombre_tentative = 0
print("Choisissait un nombre minimal et un nombre maximal pour joue a un jeu de devinette")
nombre_minimal = int(input("Entrer un nombre minimal:"))
nombre_maximal = int(input("Entrer un nombre miximal:"))
nombre_aleatoire = random.randint(nombre_minimal, nombre_maximal)
print("J'ai choisit un chiffre aleatoire entre", nombre_minimal, "et", nombre_maximal, "a vous de le deviner")
while True:
    essaie_joueur = int(input("Entrez un nombre:"))
    if essaie_joueur < nombre_aleatoire :
        nombre_tentative = nombre_tentative + 1
        print("Mauvais reponse, le nombre est plus grande que:", essaie_joueur)

    elif essaie_joueur > nombre_tentative:
        nombre_tentative = nombre_tentative + 1
        print("Mauvais reponse, le nombre est plus petit que:", essaie_joueur)

    if essaie_joueur == nombre_aleatoire:

        print("Bravo le nombre etait:", essaie_joueur, "Nombre de tentative:", nombre_tentative)
        rejouer = input("Veux tu rejouer? oui/non:")

        if rejouer == "oui" :
            pass
            nombre_tentative = 0
            print("Choisissait un nombre minimal et un nombre maximal pour joue a un jeu de devinette")
            nombre_minimal = int(input("Entrer un nombre minimal:"))
            nombre_maximal = int(input("Entrer un nombre miximal:"))
            nombre_aleatoire = random.randint(nombre_minimal, nombre_maximal)
            print("J'ai choisit un chiffre aleatoire entre", nombre_minimal, "et", nombre_maximal, "a vous de le deviner")

        elif rejouer == "non" :
            break