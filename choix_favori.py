def choix_favori():
    print ('\n--- Gestion des Favoris ---\n')
    print ('1. Ajouter un Favori')
    print ('2. Afficher les Favoris')
    print ('3. Supprimer un Favori')
    print ('4. Retour\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        from b_favori.ajouter_f import ajouter_f
        return ajouter_f()
    
    elif choice == '2':
        from b_favori.afficher_f import afficher_f
        return afficher_f()
    
    elif choice == '3':
        from b_favori.supprimer_f import supprimer_f
        return supprimer_f()
    
    elif choice == '4':
        print ()
        from choix import choix
        return choix()
    
    else:
        print ('\nChoix Impossible !\n')
        return choix_favori()