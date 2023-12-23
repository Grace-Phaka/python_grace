nombre = []
plus_grand_nombre = 0
indice = 0
for i in range(1,6):
    nombre = int(input("Entrez l'element numero " + str(i) + ":  " ))
 
       # index_grand_elment = str(nombre).index(plus_grand_nombre)
    print("Le numero "+ str(i) + "=" + ":")
    if nombre > plus_grand_nombre:
            
        plus_grand_nombre = nombre 
        indice = i
print("Le plus grand nombre est " + str(plus_grand_nombre))   
print("C'etait le nombre numéro  " + str(indice))  

