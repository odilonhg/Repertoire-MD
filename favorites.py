def favorites_f():
    
    print ('\n--- Les Favoris ---\n')
    print ('1. Ajouter un favori')
    print ('2. Afficher les favoris')
    print ('3. Supprimer un favori')
    print ('4. Menu Principal\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from fav_add import fav_add_f
        return fav_add_f()
    
    elif choice == '2':
        from fav_display import fav_display_f
        return fav_display_f()
    
    elif choice == '3':
        from fav_delete import fav_delete_f
        return fav_delete_f()
    
    elif choice == '4':
        from choice import choice_f
        return choice_f()
    
    else:
        print ('\nChoix Impossible !\n')
        return favorites_f()