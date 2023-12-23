montant = int(input("Entrez un montant : "))

devise = input("Entrez la devise : ")

taux = int(input("Entrez le taux de change en Fc "))


question = input("Voulez-vous convertir  " + str(montant) + devise + " à un taux de " + str(taux) + " ? : ")

if question == "OUI":
    
    if devise == "CDF":
        
        montant_en_dollards = montant//taux
        print(str(montant) + devise  +  " équivaut à " + str(montant_en_dollards) + " USD" )
        
    else: 
        montant_en_franc = montant*taux
        print(str(montant) + devise  +  " équivaut à " + str(montant_en_franc) + " CDF" )
else:
    montant = int(input("Entrez un autre montant: "))
    devise = input("Entrez la devise : ")

    taux = int(input("Entrez le taux de change en Fc "))
    if devise == "CDF":
        
        montant_en_dollards = montant//taux
        print(str(montant) + devise  +  " équivaut à " + str(montant_en_dollards) + " USD" )
        
    else: 
        montant_en_franc = montant*taux
        print(str(montant) + devise  +  " équivaut à " + str(montant_en_franc) + " CDF" )