from lecture_ecriture import lecture_csv
import logging
import os

liste = []

def f_rechercher():
    global liste
    f_rep = "data_contacts.csv"
    liste = lecture_csv (f_rep)
    
    print ("- Rechercher un Favori -\n")
    
    print ("1. Rechercher par prénom ou nom de famille")
    print ("2. Rechercher par numéro de téléphone")
    print ("3. Rechercher par adresse email")
    print ("4. Retour à la gestion des contacts\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            return f_nom_prenom()
        
        case "2":
            os.system ("cls")
            return f_num()
        
        case "3":
            os.system ("cls")
            return f_email()
        
        case "4":
            os.system ("cls")
            return ""
        
        case _:
            os.system ("cls")
            print ("\nChoix impossible...")
            return f_rechercher()

def f_nom_prenom():
    contact = input ("Saisir le prénom ou le nom de famille du favori à trouver : ").capitalize()
    logging.info (f"RECHERCHE FAVORI: {contact}\n")
    contact = contact.upper()
    
    contact_trouve = 0
    
    for contacts in liste:
        
        nom = contacts["nom"].upper()
        prenom = contacts["prenom"].upper()
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            if favori == "True":
                contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n- Favori/s Trouvé/s -")
        
        for contacts in liste:
            
            nom = contacts["nom"].upper()
            prenom = contacts["prenom"].upper()
            jour = contacts["jour"]
            mois = contacts["mois"]
            annee = contacts["annee"]
            num = contacts["num"]
            email = contacts["email"]
            favori = contacts["favori"]
            
            if contact == nom or contact == prenom:
                if favori == "True":
                    
                    print (f"\n|   {nom} {prenom}")
                    
                    if jour != "":
                        print (f"|   {jour} / {mois} / {annee}")
                    if num != "":
                        print (f"|   {num}")
                    if email != "":
                        print (f"|   {email}")
        
        return ""
    
    else:
        print ("\nAucun favori trouvé !")
        return ""

def f_num():
    contact = input ("Saisir le numéro de téléphone du favori à trouver : ")
    logging.info (f"RECHERCHE FAVORI: {contact}\n")
    contact_trouve = 0
    
    for contacts in liste:
        
        num = contacts["num"]
        favori = contacts["favori"]
        
        if contact == num:
            if favori == "True":
                contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n- Favori/s Trouvé/s -")
        
        for contacts in liste:
            
            nom = contacts["nom"].upper()
            prenom = contacts["prenom"].upper()
            jour = contacts["jour"]
            mois = contacts["mois"]
            annee = contacts["annee"]
            num = contacts["num"]
            email = contacts["email"]
            favori = contacts["favori"]
            
            if contact == num:
                if favori == "True":
                    
                    print (f"\n|   {nom} {prenom}")
                    
                    if jour != "":
                        print (f"|   {jour} / {mois} / {annee}")
                    if num != "":
                        print (f"|   {num}")
                    if email != "":
                        print (f"|   {email}")
        
        return ""
    
    else:
        print ("\nAucun favori trouvé !")
        return ""

def f_email():
    contact = input ("Saisir l'adresse email du favori à trouver : ")
    logging.info (f"RECHERCHE FAVORI: {contact}\n")
    contact_trouve = 0
    
    for contacts in liste:
        
        email = contacts["email"]
        favori = contacts["favori"]
        
        if contact == email:
            if favori == "True":
                contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n- Favori/s Trouvé/s -")
        
        for contacts in liste:
            
            nom = contacts["nom"].upper()
            prenom = contacts["prenom"].upper()
            jour = contacts["jour"]
            mois = contacts["mois"]
            annee = contacts["annee"]
            num = contacts["num"]
            email = contacts["email"]
            favori = contacts["favori"]
            
            if contact == email:
                if favori == "True":
                
                    print (f"\n|   {nom} {prenom}")
                    
                    if jour != "":
                        print (f"|   {jour} / {mois} / {annee}")
                    if num != "":
                        print (f"|   {num}")
                    if email != "":
                        print (f"|   {email}")
        
        return ""
    
    else:
        print ("\nAucun favori trouvé !")
        return ""