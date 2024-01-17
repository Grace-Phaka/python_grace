import json
from pathlib import Path


# affichage du dossier courant
dossier_courant = Path.cwd()
print(dossier_courant)

# afichage du dossier parent
dossier_parent = dossier_courant.parent
print(dossier_parent)

# creation du repertoire
exercice_pathlib = dossier_courant/"exercice_pathlib"
exercice_pathlib.mkdir(exist_ok=True)
print(exercice_pathlib)

#creation du fichier
bisben = exercice_pathlib/"bisben.py"
bisben.touch(exist_ok=True)
print(bisben)

# creation du fichier d'enregistrement
kilolo = exercice_pathlib/"kilolo.txt"
kilolo.touch(exist_ok=True)
print(kilolo)

# creation du fichier json
michee = exercice_pathlib/"michee.json"
michee.touch(exist_ok=True)
print(michee)

# resolution de l'exercice

print("\n")

    
name = input("Entrez votre nom svp! : ")

post_name = input("Entrez votre postnom svp! : ")

first_name = input("Entrez votre prenom svp! : ")

notice = input("Donnez votre avis svp! : ")

with open (michee, "r") as f:
    data = json.load(f)
  
    dict_info = {"nom ": name, 
                     "postnom ": post_name,
                     "prenom": first_name,
                     "avis": notice
        }
    data.append(dict_info)
        
with open (michee, "w") as ff:
        json.dump(dict_info, ff, indent= 4)
        