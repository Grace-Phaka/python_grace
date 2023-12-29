
# nombre =" 0 " 
# while nombre.isdigit() == False and nombre > 5:
#    nombre = input("Entrez un nombre compris entre 1 et 5")
ma_liste = []
menu = """
\n 1.Ajouter un élément à la liste de courses 
\n  2.Retirer un élément de la liste de courses 
\n 3.Afficher les éléments de la liste de cours5es
\n 4.Vider la liste de courses 
\n 5. Quitter le programme \n """


print("\n")

choix_menu = ["1", "2", "3", "4", "5"]
print("\n")

while True:
    print("\n")
    utilisateur = input(menu)
    print("\n")
    if utilisateur  not in choix_menu:
        print("\n")
        print("Choisissez une option valide ")
  
        continue
    print("\n")
    if utilisateur == "1": # ajouter un élement
        element = input("Entrez un élément dans la liste :  ")
        ma_liste.append(element)
        
        print("\n")
        
        print(f"L'élément {element} a bien été ajouté à la liste de courses !")
        print("\n")
      
    elif utilisateur == "2": # Retirer un élément
        
        element = input("Choisir un élément à supprimer dans la liste : ")
        
        if element in ma_liste:
            
            ma_liste.remove(element)
            
            print(f"L'élément {element} a bien été supprimer à la liste de courses !")
    
          
    elif utilisateur == "3": # afficher les éléments de la liste des courses
        print(f"Veuillez trouver votre liste de courses ci-dessous :")
        for i, element in enumerate(ma_liste, 1):
            print(f"{i}. {element}")
    elif utilisateur == "4": # Vider la liste de courses
        ma_liste.clear()
        print("La liste a été vidée !")
    elif utilisateur == "5": # Quitter le programme 
        print("Au revoir! ")
        break