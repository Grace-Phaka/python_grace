import json
from pathlib import Path

print()
print()

print("-------------------********************* Bienvenu sur votre liste des courses *********************---------------------")
print("-------------------********************* Bienvenu sur votre liste des courses *********************---------------------")



my_file_way = r"D:\Learning\Python\fichier\exer_01\file_json_01.json"


print(my_file_way)

your_nav = [
    '1. Ajouter Un élement',
    '2. Retirer un élément de la liste de courses ',
    '3. Afficher les éléments de la liste de courses',
    '4. Vider la liste de courses ',
    '5. Quitter le programme',
]

# Les différents choix de l'utilisateur
choice = """
    \n 1. Ajouter Un élement
    \n 2. Retirer un élément de la liste de courses
    \n 3. Afficher les éléments de la liste de courses
    \n 4. Vider la liste de courses 
    \n 5. Quitter le programme
"""
print('\n')


print('Votre choix doit être compris entre 1 & 5.')
print(choice)
print('\n')

user_choice = input("Entrez votre choix please : ")

print('\n')

if user_choice == '1':
    # print(your_nav[0])

    user_elment = input("Veuillez saisir l'element à ajouter dans la liste de course : ")
    print(user_choice[0])


    with open(my_file_way, "r", encoding='utf-8') as file_add:
        data = json.load(file_add)
        data.append(user_elment)


    with open(my_file_way,'w', encoding='utf-8') as file_add:

        elment_print = json.dump(data, file_add)

        print(f" votre élement {user_elment} a été ajouté avec succès")
        print('\n')

        question = input('Voulez-vous encore ajouter un element ? Oui ou Non  :  ').title()

    #------------------ ICI NOUS DONNONS LA POSSIBILITE A L'UTILISATEUR D'AJOUTER UN AUTRE SI IL LE VEUT ---------------------
    #------------------ ICI NOUS DONNONS LA POSSIBILITE A L'UTILISATEUR D'AJOUTER UN AUTRE SI IL LE VEUT ---------------------


    while question == "Oui":
        user_elment = input("Veuillez saisir l'element à ajouter dans la liste de course : ")
        print(user_choice[0])

        with open(my_file_way, "r", encoding='utf-8') as file_add:
            data = json.load(file_add)
            data.append(user_elment)


        with open(my_file_way,'w', encoding='utf-8') as file_add:

            elment_print = json.dump(data, file_add, indent=4)

            print(f" votre élement {user_elment} a été ajouté avec succès")
            question = input('Voulez-vous encore ajouter un element ? Oui ou Non : ').title()

    else:
        exit()




        #--------------- ICI NOUS DONNONS LA POSSIBILITE A L'UTILISATEUR D'AJOUTER UN AUTRE SI IL LE VEUT ------------------
        #--------------- ICI NOUS DONNONS LA POSSIBILITE A L'UTILISATEUR D'AJOUTER UN AUTRE SI IL LE VEUT ------------------



    # print(elment_print)
    # with open()
    # with open()
elif user_choice == '2':

    user_elment = input("Veuillez entrer l'élement que vous voulez retirer de la liste")
    print(user_choice[1])





elif user_choice == '3':
    # user_elment = input("Affichage")
    # print(your_nav[2])

    print("Les élements de la liste des courses sont : ")
    print('\n')

    with open(my_file_way, "r", encoding='utf-8') as file_to_print:
        result_file_to_print = json.load(file_to_print)

        print (result_file_to_print)


elif user_choice == '4':
    user_elment = input(' Vider La liste ')
    print(your_nav[3])




elif user_choice == '5':
    # user_elment = input('On quitte le programme, Au')
    print(your_nav[4])
    print(' Au revoir !!!')

    exit()


else:
    print('Erreur, Veuillez votre choix doit être ')
    exit()

