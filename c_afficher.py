from lecture_ecriture import lecture
import logging
import csv


def c_afficher():
    f_rep = "Repertoire MD.csv"
    liste = lecture(f_rep)
    
    print ("\n--- Les Contacts ---")
    print ("* = contacts favoris")
    
    logging.info ("AFFICHE: CONTACTS\n")
    
    for contacts in liste:
                
        nom = contacts["nom"]
        prenom = contacts["prenom"]
        jour = contacts["jour"]
        mois = contacts["mois"]
        annee = contacts["annee"]
        num = contacts["num"]
        email = contacts["email"]
        favori = contacts["favori"]
        
        if favori == "True":
            print (f"\n| * {nom} {prenom}")
        else:
            print (f"\n|   {nom} {prenom}")
        
        if jour != "":
            print (f"|   {jour} / {mois} / {annee}")
        if num != "":
            print (f'|   {num}')
        if email != "":
            print (f'|   {email}')
                
    from c_choix import c_choix
    return c_choix()