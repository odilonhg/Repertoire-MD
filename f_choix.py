def f_choix():
    
    print ("\n--- Gestion des Favoris ---\n")
    
    print ("1. Ajouter un favori")
    print ("2. Rechercher un favori")
    print ("3. Afficher les favoris")
    print ("4. Supprimer un favori")
    print ("5. Retour au menu principal\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            from f_ajouter import f_ajouter
            return f_ajouter()
        
        case "2":
            from f_rechercher import f_rechercher
            return f_rechercher()
        
        case "3":
            from f_afficher import f_afficher
            return f_afficher()
        
        case "4":
            from f_supprimer import f_supprimer
            return f_supprimer()
        
        case "5":
            print ()
            from choix import choix
            return choix()
        
        case _:
            print ('\nChoix impossible...')
            return f_choix()