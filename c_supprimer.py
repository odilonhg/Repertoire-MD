from lecture_ecriture import *
import sys
import logging
import os

f_rep = "data_contacts.csv"

def c_supprimer():
    liste = lecture_csv (f_rep)
    
    contact = input ("Saisir le nom ou le prénom du contact à supprimer : ").upper()
    
    for contacts in range (len (liste)):
        
        nom = liste[contacts]["nom"]
        prenom = liste[contacts]["prenom"].upper()
        
        if contact == nom or contact == prenom:
            
            if prenom == "DYLAN":
                if nom == "MESNAGE":
                    
                    print ("\nVous trouvez une pancarte, elle indique :")
                    print ("\"Ici se trouvait autrefois JoyAU, le protecteur du Créateur,")
                    print ("Si vous lisez ceci, ne supprimez pas notre créateur !\"\n")
                    print ("Le Supprimer ?")
                
                choice = input ("Choix : ").upper()
                
                if choice == "OUI":
                    os.system ("cls")
                    print ("Dommage pour toi...")
                    print (f"\nERREUR CRITIQUE: Le contact {nom} {prenom} n'a pas pu être supprimé des contacts.\n")
                    logging.info (f"ERREUR SUPPRESSION: Le Créateur.\n")
                    return ""
                    
                else:
                    os.system ("cls")
                    return ""
                    
            prenom = prenom.capitalize()
            
            choice2 = input (f"\nSupprimer le contact {nom} {prenom} (Action irréversible !) ? ").upper()
            
            if choice2 == "OUI":
                os.system ("cls")
                del (liste[contacts])
                ecriture_csv (f_rep, liste)
                print (f"Le contact {nom} {prenom} à été supprimé des contacts !\n")
                logging.info (f"SUPPRESSION CONTACT: {nom} {prenom}\n")
                return ""
    
    os.system ("cls")
    print ("Aucun contact trouvé !\n")
    return ""