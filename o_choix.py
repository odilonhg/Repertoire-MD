def o_choix():
    
    print ("\n--- Options Supplémentaires ---\n")
    
    print ("1. Supprimer un contact")
    print ("2. Accès aux Jeux")
    print ("3. Retour au menu principal\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            from c_supprimer import c_supprimer
            return c_supprimer()
        
        case "2":
            from j_choix import j_choix
            return j_choix()
        
        case "3":
            from choix import choix
            return choix()
        
        case _:
            print ("\nChoix impossible...")
            return f_choix()