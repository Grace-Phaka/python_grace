import random

nombre_myst = random.randint(0, 100)

essai = 0
print("vous avez 5 essaie" )

print("\n")

while True:
    essai = essai + 1
    print("Entrez un nombre pour la " + str(essai) + "ère fois ")
    nombre = int( input("Entrez un nombre aléatoire compris entre 0 et 100 : "))
    print("\n")
    if nombre > nombre_myst: 
        print("Ce nombre est plus grand ")
        print("\n")
    elif nombre < nombre_myst: 
        print("Ce nombre est plus petit ")
        print("\n")
    else: 
        print (f"Bravo le nombre mystère est :{nombre_myst} " )
        break
    
    if essai == 5:
        print(f"Le nombre d'essai epuisé. Le nomnre mystère était {nombre_myst} " )
        break
