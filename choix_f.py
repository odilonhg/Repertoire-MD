def choix_f():
    
    print ('\n--- Gestion des Favoris ---\n')
    
    print ('1. Ajouter un favori')
    print ('2. Rechercher un favori')
    print ('3. Afficher les favoris')
    print ('4. Supprimer un favori')
    print ('5. Retour au menu principal\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from b_favoris.ajouter_f import ajouter_f
        return ajouter_f()
    
    elif choice == '2':
        from b_favoris.rechercher_f import rechercher_f
        return rechercher_f()
    
    elif choice == '3':
        from b_favoris.afficher_f import afficher_f
        return afficher_f()
    
    elif choice == '4':
        from b_favoris.supprimer_f import supprimer_f
        return supprimer_f()
    
    elif choice == '5':
        print()
        from choix import choix
        return choix()
    
    else:
        print ('\nChoix impossible !')
        return choix_c()