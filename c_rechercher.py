from lecture_ecriture import lecture
import logging
import csv
f_rep = "Repertoire MD.csv"
liste = lecture(f_rep)

def c_rechercher():
    
    print ("\n--- Rechercher un Contact ---\n")
    
    print ("1. Rechercher par prénom ou nom de famille")
    print ("2. Rechercher par numéro de téléphone")
    print ("3. Rechercher par adresse email")
    print ("4. Autre... (jour / mois / année / état du favori)")
    print ("5. Retour à la gestion des contacts\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            return c_nom_prenom()
        
        case "2":
            return c_num()
        
        case "3":
            return c_email()
        
        case "4":
            return c_autre()
        
        case "5":
            from c_choix import c_choix
            return c_choix()
        
        case _:
            print ("\nChoix impossible...")
            return c_rechercher()

def c_nom_prenom():
    contact = input ("\nSaisir le prénom ou le nom de famille du contact à trouver : ").capitalize()
    logging.info (f"RECHERCHE CONTACT: {contact}\n")
    contact = contact.upper()
    
    contact_trouve = 0
    
    for contacts in liste:
        
        nom = contacts["nom"].upper()
        prenom = contacts["prenom"].upper()
        
        if contact == nom or contact == prenom:
            contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n--- Contact/s Trouvé/s ---")
        print ("* = contacts favoris")
        
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
                    print (f"\n| * {nom} {prenom}")
                else:
                    print (f"\n|   {nom} {prenom}")
                
                if jour != "":
                    print (f"|   {jour} / {mois} / {annee}")
                if num != "":
                    print (f"|   {num}")
                if email != "":
                    print (f"|   {email}")
        
        from c_choix import c_choix
        return c_choix()
    
    else:
        print ("\nAucun contact trouvé !")
        from c_choix import c_choix
        return c_choix()

def c_num():
    contact = input ("\nSaisir le numéro de téléphone du contact à trouver : ")
    logging.info (f"RECHERCHE CONTACT: {contact}\n")
    contact_trouve = 0
    
    for contacts in liste:
        
        num = contacts["num"]
        
        if contact == num:
            contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n--- Contact/s Trouvé/s ---")
        print ("* = contacts favoris")
        
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
                    print (f"\n| * {nom} {prenom}")
                else:
                    print (f"\n|   {nom} {prenom}")
                
                if jour != "":
                    print (f"|   {jour} / {mois} / {annee}")
                if num != "":
                    print (f"|   {num}")
                if email != "":
                    print (f"|   {email}")
        
        from c_choix import c_choix
        return c_choix()
    
    else:
        print ("\nAucun contact trouvé !")
        from c_choix import c_choix
        return c_choix()

def c_email():
    contact = input ("\nSaisir l'adresse email du contact à trouver : ")
    logging.info (f"RECHERCHE CONTACT: {contact}\n")
    contact_trouve = 0
    
    for contacts in liste:
        
        email = contacts["email"]
        
        if contact == email:
            contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n--- Contact/s Trouvé/s ---")
        print ("* = contacts favoris")
        
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
                    print (f"\n| * {nom} {prenom}")
                else:
                    print (f"\n|   {nom} {prenom}")
                
                if jour != "":
                    print (f"|   {jour} / {mois} / {annee}")
                if num != "":
                    print (f"|   {num}")
                if email != "":
                    print (f"|   {email}")
        
        from c_choix import c_choix
        return c_choix()
    
    else:
        print ("\nAucun contact trouvé !")
        from c_choix import c_choix
        return c_choix()

def c_autre():
    contact = input ("\nSaisir la donnée du contact à trouver : ")
    logging.info (f"RECHERCHE CONTACT: {contact}\n")
    contact_trouve = 0
    
    for contacts in liste:
        jour = contacts["jour"]
        mois = contacts["mois"]
        annee = contacts["annee"]
        favori = contacts["favori"]
        
        if contact == jour or contact == mois or contact == annee or contact == favori:
            contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n--- Contact/s Trouvé/s ---")
        print ("* = contacts favoris")
        
        for contacts in liste:
            
            nom = contacts["nom"].upper()
            prenom = contacts["prenom"].upper()
            jour = contacts["jour"]
            mois = contacts["mois"]
            annee = contacts["annee"]
            num = contacts["num"]
            email = contacts["email"]
            favori = contacts["favori"]
            
            if contact == jour or contact == mois or contact == annee or contact == favori:
                
                if favori == "True":
                    print (f"\n| * {nom} {prenom}")
                else:
                    print (f"\n|   {nom} {prenom}")
                
                if jour != "":
                    print (f"|   {jour} / {mois} / {annee}")
                if num != "":
                    print (f"|   {num}")
                if email != "":
                    print (f"|   {email}")
        
        from c_choix import c_choix
        return c_choix()
    
    else:
        print ("\nAucun contact trouvé !")
        from c_choix import c_choix
        return c_choix()