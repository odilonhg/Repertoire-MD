from lecture_ecriture import *
import logging
import csv
import os

f_rep = "data_contacts.csv"
liste = []

def c_rechercher ():
    global liste
    liste = lecture_csv (f_rep)
    
    print ("- Rechercher un Contact -\n")
    
    print ("1. Rechercher par prénom ou nom de famille")
    print ("2. Rechercher par numéro de téléphone")
    print ("3. Rechercher par adresse email")
    print ("4. Autre... (jour / mois / année / état du favori)")
    print ("5. Retour à la gestion des contacts\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            os.system ("cls")
            return c_nom_prenom ()
        
        case "2":
            os.system ("cls")
            return c_num ()
        
        case "3":
            os.system ("cls")
            return c_email ()
        
        case "4":
            os.system ("cls")
            return c_autre ()
        
        case "5":
            os.system ("cls")
            return ""
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case _:
            os.system ("cls")
            print ("\nChoix impossible...")
            return c_rechercher ()

def c_nom_prenom ():
    contact = input ("Saisir le prénom ou le nom de famille du contact à trouver : ").capitalize()
    logging.info (f"RECHERCHE CONTACT: {contact}\n")
    contact = contact.upper()
    
    contact_trouve = 0
    
    for contacts in liste:
        
        nom = contacts["nom"].upper()
        prenom = contacts["prenom"].upper()
        
        if contact == nom or contact == prenom:
            contact_trouve += 1
    
    if contact_trouve != 0:
        
        print ("\n- Contact/s Trouvé/s -")
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
        
        print ()
        return ""
    
    else:
        print ("\nAucun contact trouvé !\n")
        return ""

def c_num ():
    contact = input ("Saisir le numéro de téléphone du contact à trouver : ")
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
        
        print ()
        return ""
    
    else:
        print ("\nAucun contact trouvé !\n")
        return ""

def c_email ():
    contact = input ("Saisir l'adresse email du contact à trouver : ")
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
        
        print ()
        return ""
    
    else:
        print ("\nAucun contact trouvé !\n")
        return ""

def c_autre ():
    contact = input ("Saisir la donnée du contact à trouver : ")
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
        
        print ()
        return ""
    
    else:
        print ("\nAucun contact trouvé !\n")
        return ""