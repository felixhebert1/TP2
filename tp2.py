


import random

nombre_aleatoire = random.randint(0,100)
nombre_de_tentative_par_lutilisateur = 0
print("J'ai choisi un nombre entre 0 et 100 a vous de le deviner")
while True:
    nombre_entre_par_lutilisateur = int(input("Entrez un nombre:"))
    if nombre_entre_par_lutilisateur < nombre_aleatoire :
        nombre_de_tentative_par_lutilisateur = nombre_de_tentative_par_lutilisateur +1
        print("Mauvais reponse, le nombre est plus grande que:", nombre_entre_par_lutilisateur)

    elif nombre_entre_par_lutilisateur > nombre_de_tentative_par_lutilisateur:
        nombre_de_tentative_par_lutilisateur = nombre_de_tentative_par_lutilisateur +1
        print("Mauvais reponse, le nombre est plus petit que:", nombre_entre_par_lutilisateur)

    if nombre_entre_par_lutilisateur == nombre_aleatoire:

        print("Bravo le nombre etait:", nombre_entre_par_lutilisateur, "Nombre de tentative:", nombre_de_tentative_par_lutilisateur)
        reponse_de_lutilisateur_si_il_veut_rejouer = input("Veux tu rejouer? oui/non:")

        if reponse_de_lutilisateur_si_il_veut_rejouer == "oui" :
            pass
            nombre_aleatoire = random.randint(0, 100)
            nombre_de_tentative_par_lutilisateur = 0
            print("J'ai choisi un nombre entre 0 et 100 a vous de le deviner")

        elif reponse_de_lutilisateur_si_il_veut_rejouer == "non" :
            break