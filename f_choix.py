import os

from a_repertoire_md.f_ajouter import f_ajouter
from a_repertoire_md.f_rechercher import f_rechercher
from a_repertoire_md.f_afficher import f_afficher
from a_repertoire_md.f_supprimer import f_supprimer

def f_choix():
    
    print ("-- Les Favoris --\n")
    
    print ("1. Ajouter un favori")
    print ("2. Rechercher un favori")
    print ("3. Afficher les favoris")
    print ("4. Supprimer un favori")
    print ("5. Retour au menu principal\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            f_ajouter ()
            return f_choix ()
        
        case "2":
            os.system ("cls")
            f_rechercher ()
            print ()
            return f_choix ()
        
        case "3":
            os.system ("cls")
            f_afficher ()
            print ()
            return f_choix ()
        
        case "4":
            os.system ("cls")
            f_supprimer ()
            return f_choix ()
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case "5":
            return ""
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return f_choix ()