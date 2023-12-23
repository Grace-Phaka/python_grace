# paiement des impôts
# Avec les structures conditionnelles
# age = int(input("Entrez votre age : "))
# sexe = input("entrez votre sexe : ")
# if sexe == "M" and age > 20:
#     print("L'habitant est imposable ")
# elif sexe == "F" and age >= 18 and age <= 35: 
#     print("L'habitant est imposable")
# else:
#     print("L'habitant ne paie pas l'impôt ")

# Avec la boucle while

# age = 0
# sexe = ""
# while True:
#     age = int(input("Entrez votre age : "))
#     sexe = input("Entrez votre sexe : ")
#     if sexe == "M" and age > 20:
#         print("L'habitant est imposable ")
#     elif sexe == "F" and age >= 18 and age <= 35: 
#         print("L'habitant est imposable")
#     else:
#         print("L'habitant ne paie pas l'impôt ")
#         break


# Nombre parfait

# som = 0
# nombre = int(input("entrez un nombre : "))
# print("\n")

# for i in range(1,nombre):
#     if nombre % i == 0:
#         som += i

# if som == nombre: 
#     print("Ce nombre est parfait")
# else:
#     print("ce nombre n'est pas parfait ")

# Nombre d'Amstrong 
amst = 0
nbre_amst = 0
somme = 0
nombre = int(input("Entrez un nombre : "))
print("\n")
amst = nombre

while amst > 0:
    nbre_amst = amst % 10
    somme += nbre_amst ** 3
    amst //= 10

if nombre == somme:
        
        print(" ce nombre est d'amstrong ")
else:
        print("Ce nombre n'est pas d'Amstrong")
    

    

  
    
    
    