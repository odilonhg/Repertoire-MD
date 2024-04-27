from lecture_ecriture import lecture
from lecture_ecriture import ecriture
import logging
import csv


def f_ajouter():
    f_rep = "Repertoire MD.csv"
    liste = lecture(f_rep)
    
    contact = input ("\nSaisir le nom ou le prénom du contact à ajouter aux favoris : ").upper()
    
    for contacts in liste:
        
        nom = contacts["nom"]
        prenom = contacts["prenom"].upper()
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            prenom = prenom.capitalize()
            
            if favori == "True":
                print (f"\nLe contact {nom} {prenom} est déjà un contact favori !")
                from f_choix import f_choix
                return f_choix()
            
            favori = "True"
            contacts["favori"] = favori
            
            ecriture(f_rep, liste)
            
            print (f"\nLe contact {nom} {prenom} à été ajouté aux favoris !")
            logging.info (f"NOUVEAU FAVORI: {nom} {prenom}\n")
            
            from f_choix import f_choix
            return f_choix()
    
    print ('\nAucun contact trouvé !')
    from f_choix import f_choix
    return f_choix()