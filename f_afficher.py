from lecture_ecriture import lecture
import logging
import csv
f_rep = "Repertoire MD.csv"
liste = lecture(f_rep)

def f_afficher():
    global liste
    
    print ("\n--- Les Favoris ---")
    
    logging.info ("AFFICHE: FAVORIS\n")
    
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
            
            print (f"\n|   {nom} {prenom}")
        
            if jour != "":
                print (f"|   {jour} / {mois} / {annee}")
            if num != "":
                print (f'|   {num}')
            if email != "":
                print (f'|   {email}')
                
    from f_choix import f_choix
    return f_choix()