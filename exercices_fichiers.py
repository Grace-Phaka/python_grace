
print("Saisissez votre identité svp! :")
print("\n")

nom = input("Quel est votre nom ? : ")
print("\n")

post_nom = input("Quel est votre post-nom ? : ")
print("\n")

prenom = input("Quel est votre prénom ? : ")
print("\n")

print(f" je suis Mr ou Mme {nom} {post_nom} {prenom}" )
print("\n")

avis = input("donnez votre avis svp ! : ")

chemin = "D:\learningPython\exe.py"
with open (chemin, "a", encoding='utf_8') as f:
    f.write(f"Je suis Mr ou Mme {nom} {post_nom} {prenom} \n ")
    f.write(f"\n {avis} \n ")
