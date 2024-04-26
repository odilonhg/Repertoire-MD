def choix_j():
    
    print ('\n--- Centre des Jeux ---\n')
    
    print ('1. Le Chiffre Juste')
    print ('2. Le Pendu')
    print ('3. Jeu en Création... (ARRET SI LANCEMENT)')
    print ('4. Retour aux Options\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        from c_options.jeux.le_chiffre_juste import le_chiffre_juste
        return le_chiffre_juste()
    
    elif choice == '2':
        from c_options.jeux.le_pendu import le_pendu
        return le_pendu()
    
    elif choice == '3':
        pass
    
    elif choice == '4':
        from c_options.choix_o import choix_o
        return choix_o()
    
    else:
        print ('\nChoix Impossible !\n')
        return choix_j()