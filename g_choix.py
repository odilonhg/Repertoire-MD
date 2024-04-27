import os

from a_repertoire_md.g_ajouter import g_ajouter
from a_repertoire_md.g_rechercher import g_rechercher
from a_repertoire_md.g_afficher import g_afficher
from a_repertoire_md.g_modifier import g_modifier
from a_repertoire_md.g_supprimer import g_supprimer

def g_choix ():
    print ("-- Les Groupes --\n")
    
    print ("1. Ajouter un groupe")
    print ("2. Rechercher un groupe")
    print ("3. Afficher les groupes")
    print ("4. Modifier un groupe")
    print ("5. Supprimer un groupe (en BETA)")
    print ("6. Retour au Repertoire MD\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            g_ajouter ()
            return g_choix ()
        case "2":
            os.system ("cls")
            g_rechercher ()
            return g_choix ()
        case "3":
            os.system ("cls")
            g_afficher ()
            return g_choix ()
        case "4":
            os.system ("cls")
            g_modifier ()
            return g_choix ()
        case "5":
            os.system ("cls")
            print ("FONCTION EN BETA, RISQUE DE CORROMPRE LES DONNEES !")
            choice2 = input ("Continuer : ").upper ()
            if choice2 == "OUI":
                os.system ("cls")
                g_supprimer ()
                return g_choix ()
            os.system ("cls")
            return g_choix ()
        case "6":
            return ""
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return g_choix ()