som = 0
while True:
    nombre = int(input("Entrez un nombre : "))
    for i in range(1, nombre ):
        if nombre % i == 0:
            # print(i)
            som += i   
    if som == nombre:
         print("ce nombre est parfait")
    else:
        print("ce nombre n'est pas parfait ")
    # print(som) 

            
    
            