import logging
import os

from a_repertoire_md.rep_choix import rep_choix
from b_cdj.j_choix import j_choix
from c_cfs.fs_choix import fs_choix
from d_gdt.GDTv2 import gdt_choix
from e_gdmdp.GDMDPv2 import gdmdp_choix
from o_options.o_choix import o_choix

def choix():
    print ("---- Centre MD ----\n")
    
    print ("1. Répertoire de Contacts")
    print ("2. Répertoire de Jeux")
    print ("3. Centre de Fonction Spéciale")
    print ("4. Gestionnaire de Tâches")
    print ("5. Gestionnaire de MDP")
    print ("6. Options")
    print ("7. Arrêter\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            rep_choix ()
            os.system ("cls")
            return choix ()
        
        case "2":
            os.system ("cls")
            j_choix ()
            os.system ("cls")
            return choix ()
        
        case "3":
            os.system ("cls")
            fs_choix ()
            os.system ("cls")
            return choix ()
        
        case "4":
            os.system ("cls")
            gdt_choix ()
            os.system ("cls")
            return choix ()
        
        case "5":
            gdmdp_choix ()
            os.system ("cls")
            return choix ()
        
        case "6":
            os.system ("cls")
            o_choix ()
            os.system ("cls")
            return choix ()
        
        case "7":
            logging.info ("FERMETURE PROGRAMME\n")
            os._exit (0)
        
        case "13":
            os.system ("cls")
            print ("Tu as trouvé le nombre magique, utilise le partout pour revenir ici !\n")
            return choix ()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return choix ()