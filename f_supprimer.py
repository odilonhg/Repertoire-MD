from lecture_ecriture import *
import logging
import os

def f_supprimer():
    f_rep = "data_contacts.csv"
    liste = lecture_csv (f_rep)
    
    contact = input ("Saisir le nom ou le prénom du contact à supprimer des favoris : ").upper()
    
    for contacts in liste:
        
        nom = contacts["nom"]
        prenom = contacts["prenom"].upper()
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            prenom = prenom.capitalize()
            
            if favori == "True":
                choice = input (f"\nSupprimer le contact {nom} {prenom} des favoris ? ").upper()
                
                if choice == "OUI":
                    contacts["favori"] = "False"
                    ecriture_csv (f_rep, liste)
                    os.system ("cls")
                    print (f"Le contact {nom} {prenom} à été supprimé des favoris !\n")
                    logging.info (f"SUPPRESSION FAVORI: {nom} {prenom}\n")
                    return ""
                
                else:
                    os.system ("cls")
                    print ("Action annulée !\n")
                    return ""
    
    os.system ("cls")
    print ('Aucun contact trouvé !\n')
    return ""