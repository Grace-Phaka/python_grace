# nbre_fois = 0
# essai = 0
# deuxième = 0
# while True:
#     nombre = int(input("entrez un nombre : "))
#     essai = nombre
#     if nombre % 2 == 0:
#         essai /= 2
#         nbre_fois = nbre_fois + 1
#         print("le nombre " + str(nombre) + " est divisible par 2 pour la  " + str(nbre_fois) + " fois et ça donne  " + str(essai)  )
#     else:
#          print("Le nombre n'est pas divisible par 2 ")
       
#     deuxième = essai 
#     deux_valeur = 0
#     if  deuxième % 2 == 0:
#         deux_valeur = deuxième / 2
#         nbre_fois = nbre_fois + 1 
        
#         print("le nombre " + str(deuxième) + " est divisible par 2 pour la  " + str(nbre_fois) + " fois et ça donne  " + str(deux_valeur))
        
#     else:
#         print("Le nombre n'est pas divisible par 2 ")
#     break


# #  Initialisation par 0 de la plus grande valeur et de l'indice
# great_number = 0
# indice = 0

# # Ici j'au utilisé la boucle while qui va se repéter jusqu_à ce que l'utilisateur saissira 0 
# while True:
#     nombre = int(input("Veuillez saisir un nombre  numero " + str(indice) + " ou Zero si vous voulez arreter le programme.) : "))

#     if nombre == 0:
#         break
#     indice += 1

#     # Ici Je compare les nombres saisis par l'utilisateur et celui qu'on avait initialisé tout au début du script
#     if nombre > great_number:
#         great_number = nombre

#         indice_great = indice

# # Ici, Quand L'utilsateur introduit 0, je commence par vérifier si si au moins un nombre a été saisi sinon j'affiche qu'aucun nombre n'a été saisi.
# if indice > 0:
#     print("\n Le plus grand de ces nombres est :", great_number)
#     print("C'était le nombre numero", indice_great)
# else:
#     print("Prière de saisir un nombre car Vous n'en avez saisi aucun jusque-là")
    
    
# Initialisation des variables 

# indice = 0
# somme = 0
# occ = 0
# occ_sup = 0

# # Tester la boucle et la condition 

# while True:
#     nombre = int(input("input entrez un nombre numéro  " + str(indice)  + " ou zero si vous voulez arrete le programme : "))
    
#     if nombre == 0:
#         break
#     indice += 1
#     somme += nombre
#     occ = indice 
#     if nombre > 100:
#         occ_sup += 1
        
# # Affichage des éléments
 
# print("La somme de ces nombres est : " + str(somme))

# print("\n")

# print("Le nombre d'occurrence est : " + str(occ))

# print("\n")

# print("Le nombre supérieur à 100 est ou sont : " + str(occ_sup))

#nombre premier

# i = 2
# j = 0
# nombre = int(input("Entrez un nombre strictement positif : "))
# print("\n")
# if nombre <= 0: 
#     print("Ce nombre n'est pas  strictement positif ")
# else:
#     while i < nombre and nombre % i != 0:
#         i += 1
#     if i == nombre:
#      print("Les diviseurs propres sans répétition de " + str(nombre) +  " : Aucun! Il est premier ")
#     else:
       
#         print("les diviseurs propres sans répétition de " + str(nombre) + " sont : "  )
#         for j in range(2, nombre):
#             if nombre % j == 0:
#                 print(j)

# Nombre premier avec la boucle for
i = 2 

# nombre = int(input("Entrez un nombre strictement positif : "))

# print("\n")
# print("Les valeurs propres sans répétitions sont : ")
# for i in range(2, nombre):
#     if nombre % i == 0:
#         print(i)
#     else:
#         print("Premier")
#         for j in range(2, nombre):
#             if j < nombre and nombre % j != 0 :
#                 print("")
        