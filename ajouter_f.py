from pickle import *
import logging

def ajouter_f():
    
    rep = open ('MD_repertoire', 'rb')
    dico = load(rep)
    rep.close()
    
    contact = input ('\nDonnez le nom ou le prénom du contact à ajouter aux favoris : ').upper()
    
    for indice, contacts in dico.items():
        
        nom = contacts.get ('nom').upper()
        prenom = contacts.get ('prenom').upper()
        favori = contacts.get ('favori')
        
        if contact == nom or contact == prenom:
            
            if favori == True:
                print (f'\nLe contact {nom} {prenom} est déjà un contact favori !')
                from b_favoris.choix_f import choix_f
                return choix_f()
            
            dico[indice]['favori'] = True
            
            rep = open ('MD_repertoire', 'wb')
            dump (dico, rep)
            rep.close()
            
            print (f'\nLe contact {nom} {prenom} à été ajouté aux favoris !')
            logging.info (f'NOUVEAU FAVORI: {nom} {prenom}\n')
            from b_favoris.choix_f import choix_f
            return choix_f()
    
    print ('\nAucun contact trouvé !')
    from b_favoris.choix_f import choix_f
    return choix_f()