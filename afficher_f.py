from pickle import *
import os

def afficher_f():
    
    fichier_repertoire = 'MD_repertoire'
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
            
        print ('\n--- Les Contacts Favoris ---\n')
        
        for lettre_nom in alphabet:
            for lettre_prenom in alphabet:
                for i in range (len(dico.keys())):
        
                    nom = dico[i]['nom'][0]
                    prenom = dico[i]['nom'][1]
                    premiere_lettre_nom = nom[0]
                    premiere_lettre_prenom = prenom[0]
                    favori = dico[i]['favori']
                    
                    if premiere_lettre_nom.lower() == lettre_nom:
                        if premiere_lettre_prenom.lower() == lettre_prenom:
                            if favori == 'True':
                                print(f"|   {nom} {prenom}")
                                print(f"| - Numéro de téléphone : {dico[i]['num']}")
                                print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
        
        from choix import choix
        return choix()
    
    else:
        
        print ('\nAucun contact trouvé.\n')
        from choix import choix
        return choix()