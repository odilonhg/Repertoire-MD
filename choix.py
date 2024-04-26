def choix():
    print ('--- Le Répertoire ---\n')
    print ('1. Gestion des Contacts')
    print ('2. Gestion des Favoris')
    print ('3. Choix Annexes')
    print ('4. Quitter\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        from a_contact.choix_contact import choix_contact
        return choix_contact()
    
    elif choice == '2':
        from b_favori.choix_favori import choix_favori
        return choix_favori()
    
    elif choice == '3':
        from c_annexe.choix_annexe import choix_annexe
        return choix_annexe()
    
    elif choice == '4':
        return ''
    
    else:
        print ('\nChoix Impossible !\n')
        return choix()