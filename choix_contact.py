def choix_contact():
    print ('\n--- Gestion des Contacts ---\n')
    print ('1. Créer un Contact')
    print ('2. Rechercher un Contact')
    print ('3. Afficher les Contacts')
    print ('4. Modifier un Contact')
    print ('5. Supprimer un Contact')
    print ('6. Retour\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        from a_contact.ajouter_c import ajouter_c
        return ajouter_c()
    
    elif choice == '2':
        from a_contact.rechercher_c import rechercher_c
        return rechercher_c()
    
    elif choice == '3':
        from a_contact.afficher_c import afficher_c
        return afficher_c()
    
    elif choice == '4':
        from a_contact.modifier_c import modifier_c
        return modifier_c()
    
    elif choice == '5':
        from a_contact.supprimer_c import supprimer_c
        return supprimer_c()
    
    elif choice == '6':
        print ()
        from choix import choix
        return choix()
    
    else:
        print ('\nChoix Impossible !\n')
        return choix_contact()