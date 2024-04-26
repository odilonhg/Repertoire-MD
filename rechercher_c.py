from pickle import *
import os

def rechercher_c():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
        
        contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
        print()
        
        for i in range(len(dico.keys())):
        
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            favori = dico[i]['favori']
        
            if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                if favori == 'True':
                    print(f"| * {nom} {prenom}")
                    print(f"| - Numéro de téléphone : {dico[i]['num']}")
                    print(f"| - Anniversaire : {dico[i]['anniv2']}")
                    print("| - Ce contact est dans les favoris\n")
                    
                elif favori == 'False':
                    print(f"|   {nom} {prenom}")
                    print(f"| - Numéro de téléphone : {dico[i]['num']}")
                    print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
                
        from choix import choix
        return choix()

    else:
        
        print ('\nAucun contact trouvé.\n')
        from choix import choix
        return choix()