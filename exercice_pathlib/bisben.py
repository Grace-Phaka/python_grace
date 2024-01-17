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

# resolution de l'exerice
print("\n")

nom = input("Entrez votre nom svp! : ")

postnom = input("Entrez votre postnom svp! : ")

prenom = input("Entrez votre prenom svp! : ")

avis = input("Donnez votre avis svp! : ")

with open(kilolo,"a", encoding="utf_8") as f:
    f.write(f" \n Je suis Mr ou Mme {nom} {postnom} {prenom} mon avis est le suivant : {avis} ")

#creation d'un nouveau fichier python

phaka = exercice_pathlib/"phaka.py"
phaka.touch(exist_ok=True)
print(phaka)


