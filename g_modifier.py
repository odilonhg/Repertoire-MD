from lecture_ecriture import *
import logging
import os

f_groupes = "data_groupes.csv"
f_rep = "data_contacts.csv"

def g_modifier ():
    liste = lecture_csv (f_rep)
    liste_g = lecture_csv (f_groupes)
    
    print ("- Modifier un Groupe -\n")
    
    print ("0. Annuler")
    print ("1. Ajouter un membre")
    print ("2. Supprimer un membre\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            os.system ("cls")
            return ""
        
        case "1":
            os.system ("cls")
            nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
            
            for groupe in liste_g:
                if nom_groupe == groupe["nom"].upper () or nom_groupe == groupe["num"]:
                    nom = groupe["nom"]
                    num = groupe["num"]
                    nbr_mbr = groupe["nbr_mbr"]
                    
                    print (f"\n| {num}. {nom}")
                    print (f"|    Membres : {nbr_mbr}/100")
                    
                    for membre in liste:
                        membre_num = list (membre["groupe"])
                        membre_nom = membre["nom"]
                        membre_prenom = membre["prenom"]
                        
                        if num in membre_num:
                            print (f"|")
                            print (f"|    {membre_nom} {membre_prenom}")
                    
                    contact = input ("\nSaisir le nom ou le prénom du contact à ajouter au groupe : ").upper ()
                    
                    for contacts in liste:
                        nom_c = contacts["nom"]
                        prenom_c = contacts["prenom"].upper ()
                        
                        if contact == nom_c or contact == prenom_c:
                            int_nbr_mbr = int (nbr_mbr)
                            int_nbr_mbr += 1
                            nbr_mbr = str (int_nbr_mbr)
                            contacts["groupe"] += str (num)
                            ecriture_csv (f_rep, liste)
                            ecriture_csv (f_groupes, liste_g)
                            logging.info (f"NOUVEAU CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize ()}\n")
                            os.system ("cls")
                            print (f"Le contact {nom_c} {prenom_c.capitalize()} a été ajouté au groupe {nom} !")
                            return ""
            
            os.system ("cls")
            return ""
        
        case "2":
            os.system ("cls")
            nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
            
            for groupe in liste_g:
                if nom_groupe == groupe["nom"].upper () or nom_groupe == groupe["num"]:
                    nom = groupe["nom"]
                    num = groupe["num"]
                    nbr_mbr = groupe["nbr_mbr"]
                    
                    print (f"\n| {num}. {nom}")
                    print (f"|    Membres : {nbr_mbr}/100")
                    
                    for membre in liste:
                        membre_num = list (membre["groupe"])
                        membre_nom = membre["nom"]
                        membre_prenom = membre["prenom"]
                        
                        if num in membre_num:
                            print (f"|")
                            print (f"|    {membre_nom} {membre_prenom}")
                    
                    contact = input ("\nSaisir le nom ou le prénom du contact à ajouter au groupe : ").upper ()
                    
                    for contacts in liste:
                        nom_c = contacts["nom"]
                        prenom_c = contacts["prenom"].upper ()
                        num_c = list (contacts["groupe"])
                        
                        if contact == nom_c or contact == prenom_c:
                            new_num = ""
                            for i in range (len (num_c)):
                                if num_c[i] != num:
                                    new_num += num_c[i]
                            contacts["groupe"] = str (new_num)
                            int_nbr_mbr = int (nbr_mbr)
                            int_nbr_mbr -= 1
                            nbr_mbr = str (int_nbr_mbr)
                            ecriture_csv (f_rep, liste)
                            ecriture_csv (f_groupes, liste_g)
                            os.system ("cls")
                            print (f"Le contact {nom_c} {prenom_c.capitalize()} a été supprimé du groupe !\n")
                            logging.info (f"SUPPRESSION DU CONTACT DANS {nom}: {nom_c} {prenom_c.capitalize()}\n")
                            return ""
            
            os.system ("cls")
            return ""
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return g_modifier ()