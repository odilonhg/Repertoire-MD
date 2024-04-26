from pickle import *
import logging

choice = 'NONE'

rep = open ('MD_repertoire', 'rb')
dico = load (rep)
rep.close()

def rechercher_f():
    
    global choice
    
    print ('\n--- Rechercher un Contact ---\n')
    
    print ('1. Rechercher par prénom ou nom de famille')
    print ('2. Rechercher par numéro de téléphone')
    print ('3. Rechercher par adresse email')
    print ('4. Retour à la gestion des contacts\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        return rechercher_favori()
    
    elif choice == '2':
        return rechercher_favori()
    
    elif choice == '3':
        return rechercher_favori()
    
    elif choice == '4':
        from b_favoris.choix_f import choix_f
        return choix_f()
    
    else:
        print('\nChoix impossible !\n')
        return rechercher_f()

def rechercher_favori():
    
    global choice, dico
    
    if choice == '1':
        contact = input ('\nSaisir le prénom ou le nom de famille du favori à trouver : ').upper()
    
    elif choice == '2':
        contact = input ('\nSaisir le numéro de téléphone du favori à trouver : ')
    
    elif choice == '3':
        contact = input ('\nSaisir l\'adresse email du favori à trouver : ')
    
    choice = 'NONE'
    
    print ('\n--- Favori/s Trouvé/s ---')
    
    favori_trouve = 0
    
    logging.info (f'Recherche favori: {contact}\n')
    
    for indice, contacts in dico.items():
        
        nom = contacts.get ('nom').upper()
        prenom = contacts.get ('prenom').upper()
        
        jour = contacts.get ('jour', None)
        mois = contacts.get ('mois', None)
        annee = contacts.get ('annee', None)
        num = contacts.get ('num', None)
        email = contacts.get ('email', None)
        favori = contacts.get ('favori', False)
        
        if contact == nom or contact == prenom or contact == num or contact == email:
            if favori == True:
                
                print (f'\n|   {nom} {prenom}')
                
                if jour is not None:
                    print (f'|   {jour} / {mois} / {annee}')
                if num is not None:
                    print (f'|   {num}')
                if email is not None:
                    print (f'|   {email}')
            
                favori_trouve += 1
                
    if favori_trouve != 0:
        from b_favoris.choix_f import choix_f
        return choix_f()
    
    else:
        print ('\nAucun contact trouvé !')
        from b_favoris.choix_f import choix_f
        return choix_f()