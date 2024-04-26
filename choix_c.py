def choix_c():
    
    print ('\n--- Gestion des Contacts ---\n')
    
    print ('1. Ajouter un contact')
    print ('2. Rechercher un contact')
    print ('3. Afficher les contacts')
    print ('4. Modifier un contact')
    print ('5. Retour au menu principal\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from a_contacts.ajouter_c import ajouter_c
        return ajouter_c()
    
    elif choice == '2':
        from a_contacts.rechercher_c import rechercher_c
        return rechercher_c()
    
    elif choice == '3':
        from a_contacts.afficher_c import afficher_c
        return afficher_c()
    
    elif choice == '4':
        from a_contacts.modifier_c import modifier_c
        return modifier_c()
    
    elif choice == '5':
        print()
        from choix import choix
        return choix()
    
    else:
        print ('\nChoix impossible !')
        return choix_c()