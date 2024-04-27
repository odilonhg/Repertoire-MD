import os

from a_repertoire_md.c_ajouter import c_ajouter
from a_repertoire_md.c_rechercher import c_rechercher
from a_repertoire_md.c_afficher import c_afficher
from a_repertoire_md.c_modifier import c_modifier
from a_repertoire_md.c_supprimer import c_supprimer

def c_choix():
    print ("-- Les Contacts --\n")
    
    print ("1. Ajouter un contact")
    print ("2. Rechercher un contact")
    print ("3. Afficher les contacts")
    print ("4. Modifier un contact")
    print ("5. Supprimer un contact")
    print ("6. Retour au Repertoire MD\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            c_ajouter ()
            return c_choix ()
        
        case "2":
            os.system ("cls")
            c_rechercher ()
            return c_choix ()
        
        case "3":
            os.system ("cls")
            c_afficher ()
            print ()
            return c_choix ()
        
        case "4":
            os.system ("cls")
            c_modifier ()
            return c_choix ()
        
        case "5":
            os.system ("cls")
            c_supprimer ()
            return c_choix ()
        
        case "6":
            return ""
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return c_choix ()