from lecture_ecriture import joyau
from lecture_ecriture import lecture
from lecture_ecriture import ecriture
import sys
import logging
import csv
f_rep = "Repertoire MD.csv"
liste = lecture(f_rep)

def c_supprimer():
    global liste, joyau
    
    contact = input ("\nSaisir le nom ou le prénom du contact à supprimer des favoris : ").upper()
    
    for contacts in range (len (liste)):
        
        nom = liste[contacts]["nom"]
        prenom = liste[contacts]["prenom"].upper()
        
        if contact == nom or contact == prenom:
            
            if prenom == "DYLAN":
                
                print ("\nOulaaa, doucement !")
                print ("Salut, moi c'est JoyAU, éternel défenseur de Dylan, le créateur de ce répertoire !")
                print ("Si jamais tu t'arrêtes là et si tu laisses Dylan tranquille, je t'offres mon joyau !")
                print ("T'es d'accord ?\n")
                
                choice = ("Choix : ").upper()
                
                if choice == "OUI":
                    print ("Super !")
                    print ("Voilà ton joyau !")
                    print ("A la prochaine !")
                    
                    joyau += 1
                    
                    from o_choix import o_choix
                    return o_choix()
                    
                else:
                    print ("Dommage pour toi !")
                    logging.info("MOI, JOYAU, J'AI FERME LE PROGRAMME POUR PROTEGER DYLAN !\n")
                    sys.exit("FERMETURE FORCEE !")
                    
            prenom = prenom.capitalize()
            
            choice2 = input (f"\nSupprimer le contact {nom} {prenom} (Action irréversible !) ? ").upper()
            
            if choice2 == "OUI":
                del (liste[contacts])
                ecriture(f_rep, liste)
                print (f"\nLe contact {nom} {prenom} à été supprimé des favoris !")
                logging.info (f"SUPPRESSION CONTACT: {nom} {prenom}\n")
                from o_choix import o_choix
                return o_choix()
                
            else:
                print ("\nAction annulée !")
                from o_choix import o_choix
                return o_choix()
                
    print ('\nAucun contact trouvé !')
    from o_choix import o_choix
    return o_choix()