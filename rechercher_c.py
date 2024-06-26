from pickle import *
import logging

choice = 'NONE'

rep = open ('MD_repertoire', 'rb')
dico = load (rep)
rep.close()

def rechercher_c():
    
    global choice
    
    print ('\n--- Rechercher un Contact ---\n')
    
    print ('1. Rechercher par prénom ou nom de famille')
    print ('2. Rechercher par numéro de téléphone')
    print ('3. Rechercher par adresse email')
    print ('4. Retour à la gestion des contacts\n')
    
    choice = input ('Choix : ')
    
    if choice == '1':
        return rechercher_contact()
    
    elif choice == '2':
        return rechercher_contact()
    
    elif choice == '3':
        return rechercher_contact()
    
    elif choice == '4':
        from a_contacts.choix_c import choix_c
        return choix_c()
    
    else:
        print('\nChoix impossible !\n')
        return rechercher_c()

def rechercher_contact():
    
    global choice, dico
    
    if choice == '1':
        contact = input ('\nSaisir le prénom ou le nom de famille du contact à trouver : ').upper()
    
    elif choice == '2':
        contact = input ('\nSaisir le numéro de téléphone du contact à trouver : ')
    
    elif choice == '3':
        contact = input ('\nSaisir l\'adresse email du contact à trouver : ')
    
    choice = 'NONE'
    
    print ('\n--- Contact/s Trouvé/s ---')
    print ('* = contacts favoris')
    
    contact_trouve = 0
    
    logging.info (f'Recherche: {contact}\n')
    
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
                print (f'\n| * {nom} {prenom}')
            else:
                print (f'\n|   {nom} {prenom}')
            
            if jour is not None:
                print (f'|   {jour} / {mois} / {annee}')
            if num is not None:
                print (f'|   {num}')
            if email is not None:
                print (f'|   {email}')
            
            contact_trouve += 1
    
    if contact_trouve != 0:
        from a_contacts.choix_c import choix_c
        return choix_c()
    
    else:
        print ('\nAucun contact trouvé !')
        from a_contacts.choix_c import choix_c
        return choix_c()