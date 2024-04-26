from pickle import *
import os

def supprimer_f():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
        
        contact_recherche = input('\nDonnez le nom ou le prénom du contact à supprimer de vos favoris : ')
        
        for i in range (len(dico.keys())):
            
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            
            if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                dico[i]['favori'] = 'False'
                
                rep = open ('MD_repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {nom} {prenom} à été supprimé des favoris !\n')
                from choix import choix
                return choix()
        
        print ('\nAucun contact trouvé.\n')
        from choix import choix
        return choix()
        
    else:
        
        print ('\nAucun contact trouvé.\n')
        from choix import choix
        return choix()