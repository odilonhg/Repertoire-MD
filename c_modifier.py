from lecture_ecriture import lecture
from lecture_ecriture import ecriture
import logging
import csv
f_rep = "Repertoire MD.csv"
liste = lecture(f_rep)

def c_modifier():
    global liste, f_rep
    
    print ("\n--- Modifier un Contact ---\n")
    
    print ("0. Annuler !")
    print ("1. Modifier le nom")
    print ("2. Modifier le prénom")
    print ("3. Modifier la date de naissance")
    print ("4. Modifier le numéro de téléphone")
    print ("5. Modifier l'adresse email\n")
    
    choice = input ('Choix : ')
    
    if choice == "0":
        from c_choix import c_choix
        return c_choix()
    
    elif choice == "13":
        print ("\nT'es sérieux/euse là ?\n")
        from choix import choix
        return choix()
    
    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print ("\nChoix impossible...")
        return c_modifier()
    
    contact = input ('\nSaisir le nom ou le prénom du contact : ').upper()
    
    for contacts in liste:
                
        nom = contacts["nom"]
        prenom = contacts["prenom"].upper()
        jour = contacts["jour"]
        mois = contacts["mois"]
        annee = contacts["annee"]
        num = contacts["num"]
        email = contacts["email"]
        favori = contacts["favori"]
        
        if contact == nom or contact == prenom:
            prenom = prenom.capitalize()
            old_nom = contacts["nom"]
            old_prenom = contacts["prenom"]
            
            match choice:
                
                case "1":
                    nom = input (f"\nSaisir le nouveau nom de {nom} {prenom} : ").upper()
                    contacts["nom"] = nom
                    logging.info (f"MODIFIE: {old_nom} -> {nom} | ({old_nom} {prenom})\n")
                    
                case "2":
                    prenom = input (f"\nSaisir le nouveau prénom de {nom} {prenom} : ").capitalize()
                    contacts["prenom"] = prenom
                    logging.info (f"MODIFIE: {old_prenom} -> {prenom} | ({nom} {old_prenom})\n")
                    
                case "3":
                    jour = input (f"\nSaisir le jour de naissance de {nom} {prenom} : ")
                    mois = input (f"\nSaisir le mois de naissance de {nom} {prenom} : ")
                    annee = input (f"\nSaisir l'année de naissance de {nom} {prenom} : ")
                    old_jour = contacts["jour"]
                    old_mois = contacts["mois"]
                    old_annee = contacts["annee"]
                    contacts["jour"] = jour
                    contacts["mois"] = mois
                    contacts["annee"] = annee
                    logging.info (f"MODIFIE: {old_jour}/{old_mois}/{old_annee} -> {jour}/{mois}/{annee} | ({nom} {prenom})\n")
                    
                case "4":
                    num = input (f"\nSaisir le nouveau numéro de téléphone de {nom} {prenom} : ")
                    old_num = contacts["num"]
                    contacts["num"] = num
                    logging.info (f"MODIFIE: {old_num} -> {num} | ({nom} {prenom})\n")
                    
                case "5":
                    email = input (f"\nSaisir la nouvelle adresse email de {nom} {prenom} : ")
                    old_email = contacts["email"]
                    contacts["email"] = email
                    logging.info (f"MODIFIE: {old_email} -> {email} | ({nom} {prenom})\n")
            
            ecriture(f_rep, liste)
            
            print (f"\nLe contact {old_nom} {old_prenom} a été modifié !")
            from c_choix import c_choix
            return c_choix()
        
        else:
            print ("\nAucun contact trouvé !")
            from c_choix import c_choix
            return c_choix()