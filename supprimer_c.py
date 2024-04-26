from pickle import *
import os

def supprimer_c():
    
    print ('\nATTENTION, cette action est irréversible !')
    
    avertissement = input ('\nTappez "oui" pour confirmer ou "non" pour annuler : ')
    
    while avertissement != 'oui' and avertissement != 'non':
        avertissement = input ('\nRéponse invalide. Veuillez taper "oui" pour confirmer ou "non" pour annuler : ')
        
    if avertissement == 'non':
        print ('\nAction annulée\n')
        from choix import choix
        return choix()
    
    elif avertissement=='oui':
        
        fichier_repertoire = 'MD_repertoire'

        if os.path.exists (fichier_repertoire):
        
            rep = open ('MD_repertoire', 'rb')
            dico = load(rep)
            rep.close()
    
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact à supprimer : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
            
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                    
                    del dico[i]
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été supprimé !\n')
                    
                    from choix import choix
                    return choix()
            
            print ('\nAucun contact trouvé.\n')
            from choix import choix
            return choix()
        
        else:
        
            print ('\nAucun contact trouvé.\n')
            from choix import choix
            return choix()