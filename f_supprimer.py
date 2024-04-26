from lecture_ecriture import lecture
from lecture_ecriture import ecriture
import logging
import csv
f_rep = "Repertoire MD.csv"
liste = lecture(f_rep)

def f_supprimer():
    global liste
    
    contact = input ("\nSaisir le nom ou le prénom du contact à supprimer des favoris : ").upper()
    
    for contacts in liste:
        
        nom = contacts["nom"]
        prenom = contacts["prenom"].upper()
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            prenom = prenom.capitalize()
            
            if favori == "True":
                choice = input (f"\nSupprimer le contact {nom} {prenom} des favoris ? ").upper()
                
                if choice == "OUI":
                    favori = "False"
                    contacts["favori"] = favori
                    ecriture(f_rep, liste)
                    print (f"\nLe contact {nom} {prenom} à été supprimé des favoris !")
                    logging.info (f"SUPPRESSION FAVORI: {nom} {prenom}\n")
                    from f_choix import f_choix
                    return f_choix()
                
                else:
                    print ("\nAction annulée !")
                    from f_choix import f_choix
                    return f_choix()
    
    print ('\nAucun contact trouvé !')
    from f_choix import f_choix
    return f_choix()