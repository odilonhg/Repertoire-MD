from pickle import *
import logging

def supprimer_c():
    
    rep = open ('MD_repertoire', 'rb')
    dico = load(rep)
    rep.close()
    
    contact = input ('\nSaisir le nom ou le prénom du contact à supprimer (pour annuler, pressez espace) : ').upper()
    
    if contact == '':
        from c_options.choix_o import choix_o
        return choix_o()
    
    for indice, contacts in dico.items():
        
        nom = contacts.get ('nom').upper()
        prenom = contacts.get ('prenom').upper()
    
        if contact == nom or contact == prenom:
            
            del dico[indice]
            prenom = contacts.get ('prenom').capitalize()
            print (f'\nLe contact {nom} {prenom} a été supprimé !')
            logging.info(f'SUPPRESSION CONTACT: {nom} {prenom}\n')
            
            rep = open ('MD_repertoire', 'wb')
            dump (dico, rep)
            rep.close()
            
            from c_options.choix_o import choix_o
            return choix_o()
    
    print ('\nAucun contact trouvé !')
    from c_options.choix_o import choix_o
    return choix_o()
            