def c_choix():
    
    print ("\n--- Gestion des Contacts ---\n")
    
    print ("1. Ajouter un contact")
    print ("2. Rechercher un contact")
    print ("3. Afficher les contacts")
    print ("4. Modifier un contact")
    print ("5. Retour au menu principal\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            from c_ajouter import c_ajouter
            return c_ajouter()
        
        case "2":
            from c_rechercher import c_rechercher
            return c_rechercher()
        
        case "3":
            from c_afficher import c_afficher
            return c_afficher()
        
        case "4":
            from c_modifier import c_modifier
            return c_modifier()
        
        case "5":
            print ()
            from choix import choix
            return choix()
        
        case "13":
            print ("Oh, le chiffre préféré de JoyO !")
            print ("Je paries que tu peux le trouver au menu principal.\n")
            return c_choix()
        
        case _:
            print ("\nChoix impossible...")
            return c_choix()