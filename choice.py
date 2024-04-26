def choice_f():
    
    print ('--- Le Répertoire ---\n')
    print ('1. Ajouter un contact')
    print ('2. Afficher les contacts')
    print ('3. Rechercher un contact')
    print ('4. Gérer les favoris')
    print ('5. Options Spéciales')
    print ('6. Arrêter\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from add import add_f
        return add_f()
    
    elif choice == '2':
        from display import display_f
        return display_f()
    
    elif choice == '3':
        from research import research_f
        return research_f()
    
    elif choice == '4':
        from favorites import favorites_f
        return favorites_f()
    
    elif choice == '5':
        from options import options_f
        return options_f()
    
    elif choice == '6':
        return ''
    
    else:
        print ('\nChoix Impossible !\n')
        return choice_f()