from lecture_ecriture import *
import logging
import os

def f_ajouter ():
    f_rep = "data_contacts.csv"
    liste = lecture_csv (f_rep)
    
    contact = input ("Saisir le nom ou le prénom du contact à ajouter aux favoris : ").upper()
    
    for contacts in liste:
        
        nom = contacts["nom"]
        prenom = contacts["prenom"].upper()
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            prenom = prenom.capitalize()
            
            if favori == "True":
                os.system ("cls")
                print (f"Le contact {nom} {prenom} est déjà un contact favori !\n")
                return ""
            
            contacts["favori"] = "True"
            ecriture_csv (f_rep, liste)
            
            os.system ("cls")
            print (f"Le contact {nom} {prenom} à été ajouté aux favoris !\n")
            logging.info (f"NOUVEAU FAVORI: {nom} {prenom}\n")
            
            return ""
    
    os.system ("cls")
    print ('Aucun contact trouvé !\n')
    return ""