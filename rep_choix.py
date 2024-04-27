import os
from a_repertoire_md.c_choix import c_choix
from a_repertoire_md.f_choix import f_choix
from a_repertoire_md.g_choix import g_choix

def rep_choix ():
    print ("--- Répertoire MD ---\n")
    
    print ("1. Gérer les contacts")
    print ("2. Gérer les favoris")
    print ("3. Gérer les groupes (NOUVEAU !)")
    print ("4. Retour au menu\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            c_choix ()
            os.system ("cls")
            return rep_choix ()
        
        case "2":
            os.system ("cls")
            f_choix ()
            os.system ("cls")
            return rep_choix ()
        
        case "3":
            os.system ("cls")
            g_choix ()
            os.system ("cls")
            return rep_choix ()
        
        case "4":
            return ""
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return rep_choix ()