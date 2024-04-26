def options_f():
    
    print ('\n--- Options Spéciales ---\n')
    print ('1. Supprimer un contact')
    print ('2. Modifier un contact')
    print ('3. Menu Principal\n')
    print ('4. Option SUPER MEGA Spéciale ULTRA 3000\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from delete import delete_f
        return delete_f()
    
    elif choice == '2':
        from modify import modify_f
        return modify_f()
    
    elif choice == '3':
        from choice import choice_f
        return choice_f()
    
    elif choice == '4':
        from opt_special import opt_special_f
        return opt_special_f()
    
    else:
        print ('\nChoix Impossible !\n')
        return options_f()