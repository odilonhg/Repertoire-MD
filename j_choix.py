def j_choix():
    
    print ("\n--- Centre des Jeux ---\n")
    
    print ("1. Le Chiffre Juste")
    print ("2. Le Pendu")
    print ("3. Le Puissance 4 (NOUVEAU !)")
    print ("4. Jeu en création...")
    print ("5. Retour aux Options\n")
    
    choice = input ("Choix : ")
    
    if choice == "1":
        from j_chiffre_juste import j_chiffre_juste
        return j_chiffre_juste()
    
    elif choice == "2":
        from j_pendu import j_pendu
        return j_pendu()
    
    elif choice == "3":
        print ()
        from j_puissance_4 import j_puissance_4
        return j_puissance_4()
    
    elif choice == "4":
        print ("\nJeu en création...\n")
        return j_choix()
    
    elif choice == "5":
        from o_choix import o_choix
        return o_choix()
    
    else:
        print ("\nChoix Impossible...\n")
        return j_choix()