from lecture_ecriture import *
import logging
import os
f_rep = "data_contacts.csv"
f_groupes = "data_groupes.csv"

liste = []
liste_g = []

num = 0
nom = ""
nbr_mbr = 0

def g_ajouter ():
    global liste, liste_g, num, nom, nbr_mbr
    
    liste = lecture_csv (f_rep)
    liste_g = lecture_csv (f_groupes)
    num = len(liste_g) + 1
    num = str (num)
    
    print ("- Ajouter un Groupe -\n")
    
    print ("0. Annuler")
    print ("1. Le nom du groupe")
    print ("2. Les membres du groupe (optionnel)")
    print ("3. Finir le groupe !\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            os.system ("cls")
            return ""
        
        case "1":
            if nom == "":
                os.system ("cls")
                nom = input ("Saisir le nom du groupe : ")
                logging.info (f"NOUVEAU GROUPE: {nom}\n")
                os.system ("cls")
                return g_ajouter()
            else:
                os.system ("cls")
                return g_ajouter ()
        
        case "2":
            os.system ("cls")
            contact = input ("Saisir le nom ou le prénom du contact à ajouter au groupe : ").upper ()
            
            for contacts in liste:
                nom_c = contacts["nom"]
                prenom_c = contacts["prenom"].upper ()
                
                if contact == nom_c or contact == prenom_c:
                    choice2 = input (f"\nAjouter {nom_c} {prenom_c.capitalize ()} : ").upper ()
                    
                    if choice2 == "OUI":
                        nbr_mbr += 1
                        contacts["groupe"] += num
                        ecriture_csv (f_rep, liste)
                        logging.info (f"NOUVEAU CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize ()}\n")
                        os.system ("cls")
                        return g_ajouter ()
            
            os.system ("cls")
            print ("Aucun contact trouvé !\n")
            return g_ajouter ()
        
        case "3":
            os.system ("cls")
            if nom == "":
                nom = input ("Saisir le nom du groupe : ")
                print ()
            
            g_new = {"num": num, "nom": nom, "nbr_mbr": str (nbr_mbr)}
            liste_g.append (g_new)
            ecriture_csv (f_groupes, liste_g)
            
            print (f"Le groupe {nom} a été crée !\n")
            return ""
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return g_ajouter ()