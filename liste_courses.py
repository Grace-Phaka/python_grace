import json
import os

cur_dir = os.path.dirname(__file__)
liste_path = os.path.join(cur_dir, "liste.json")

# nombre =" 0 " 
# while nombre.isdigit() == False and nombre > 5:
#    nombre = input("Entrez un nombre compris entre 1 et 5")
ma_liste = []
menu = """
\n 1.Ajouter un élément à la liste de courses 
\n  2.Retirer un élément de la liste de courses 
\n 3.Afficher les éléments de la liste de courses
\n 4.Vider la liste de courses 
\n 5. Quitter le programme \n """


print("\n")

choix_menu = [1, 2, 3, 4, 5]
print("\n")
if os.path.exists(liste_path):
    with open(liste_path, "r") as f:
        liste = json.load(f)
        
else: 
    liste = []

while True:
    print("\n")
    utilisateur = int(input(menu))
    print("\n")
    if utilisateur  not in choix_menu:
        print("\n")
        print("Choisissez une option valide ")
  
        continue
    print("\n")
    if utilisateur == 1: # ajouter un élement
        element = input("Entrez un élément dans la liste :  ")
        ma_liste.append(element)
        
        print("\n")
        
        print(f"L'élément {element} a bien été ajouté à la liste de courses !")
        print("\n")
      
    elif utilisateur == 2: # Retirer un élément
        
        element = int(input("Choisir un élément à supprimer dans la liste : "))
        print(element)
        
        if element in ma_liste:
            
            ma_liste.pop(element)
            
            print(f"L'élément {element} a bien été supprimer à la liste de courses !")
    
          
    elif utilisateur == 3: # afficher les éléments de la liste des courses
        print(f"Veuillez trouver votre liste de courses ci-dessous :")
        for i, element in enumerate(ma_liste, 1):
            print(f"{i}. {element}")
    elif utilisateur == 4: # Vider la liste de courses
        ma_liste.clear()
        print("La liste a été vidée !")
    elif utilisateur == 5: # Quitter le programme 
        with open(liste_path, "w") as f:
            json.dump(liste, f, indent=2)
            print("Au revoir! ")
            break