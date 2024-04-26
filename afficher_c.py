from pickle import *
import logging

def afficher_c():
    
    rep = open ('MD_repertoire', 'rb')
    dico = load (rep)
    rep.close()
    
    print ('\n--- Les Contacts ---')
    print ('* = contacts favoris')
    
    logging.info ('Affichage des contacts\n')
    
    for indice, contacts in dico.items():
                
        nom = contacts.get ('nom').upper()
        prenom = contacts.get ('prenom').upper()
        
        jour = contacts.get ('jour', None)
        mois = contacts.get ('mois', None)
        annee = contacts.get ('annee', None)
        num = contacts.get ('num', None)
        email = contacts.get ('email', None)
        favori = contacts.get ('favori', False)
        
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
                
    from a_contacts.choix_c import choix_c
    return choix_c()