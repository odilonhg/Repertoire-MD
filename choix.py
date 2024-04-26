import sys
import logging

def choix():
    
    print ('--- MD_Répertoire ---\n')
    
    print ('1. Gérer les contacts')
    print ('2. Gérer les favoris')
    print ('3. Options')
    print ('4. Arrêter\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        from a_contacts.choix_c import choix_c
        return choix_c()
    
    elif choice == '2':
        from b_favoris.choix_f import choix_f
        return choix_f()
    
    elif choice == '3':
        from c_options.choix_o import choix_o
        return choix_o()
    
    elif choice == '4':
        logging.info('FERMETURE PROGRAMME\n')
        sys.exit('Fermeture du programme')
    
    else:
        print ('\nChoix impossible...\n')
        return choix()