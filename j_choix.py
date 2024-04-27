import os

from b_cdj.j_chiffre_juste import j_chiffre_juste
from b_cdj.j_pendu import j_pendu
from b_cdj.j_puissance_4 import j_puissance_4
from b_cdj.j_morpion import j_morpion


def j_choix ():
    print ("--- Répertoire de Jeux MD ---\n")
    
    print ("1. Le Chiffre Juste")
    print ("2. Le Pendu")
    print ("3. Le Puissance 4")
    print ("4. Le Morpion (NOUVEAU !)")
    print ("5. Retour au menu\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            j_chiffre_juste ()
            return j_choix ()
        
        case "2":
            os.system ("cls")
            j_pendu ()
            return j_choix ()
        
        case "3":
            os.system ("cls")
            j_puissance_4 ()
            return j_choix ()
        
        case "4":
            os.system ("cls")
            j_morpion ()
            return j_choix ()
        
        case "5":
            return ""
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()