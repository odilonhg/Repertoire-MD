def choix_o():
    
    print ('\n--- Options Supplémentaires ---\n')
    
    print ('1. Supprimer un contact')
    print ('2. Accès aux jeux')
    print ('3. Retour au menu principal\n')
    
    print ('?. Fonction spéciale !\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        from c_options.supprimer_c import supprimer_c
        return supprimer_c()
    
    elif choice == '2':
        from c_options.jeux.choix_j import choix_j
        return choix_j()
    
    elif choice == '3':
        print ()
        from choix import choix
        return choix()
    
    elif choice == '?':
        from c_options.fonction_super_mega_speciale_4001 import fonction_super_mega_speciale_4001
        return fonction_super_mega_speciale_4001()
    
    elif choice == 'pass':
        pass
    
    elif choice == 'pass':
        pass
    
    else:
        print ('\nChoix Impossible !\n')
        return choix_o()
    
# from c_annexe.(fonction) import fonction