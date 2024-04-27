from lecture_ecriture import lecture_csv
import logging

def f_afficher():
    f_rep = "data_contacts.csv"
    liste = lecture_csv (f_rep)
    
    print ("- Les Favoris -")
    
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
                
    return ""