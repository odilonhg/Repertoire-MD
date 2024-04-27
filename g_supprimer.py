from lecture_ecriture import *
import os
import logging

f_rep = "data_contacts.csv"
f_groupes = "data_groupes.csv"

def g_supprimer ():
    liste_g = lecture_csv (f_groupes)
    liste = lecture_csv (f_rep)
    nom_groupe = input ("Saisir le nom ou le numéro du groupe à supprimer : ").upper ()
    if nom_groupe == "LES CRÉATEURS":
        os.system ("cls")
        print ("Choix impossible...\n")
        return ""
            
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
            
            choice = input (f"\nSupprimer {nom} : ").upper ()
            if choice == "OUI":
                
                os.system ("cls")
                new_liste_g = []
                for groupe in liste_g:
                    if groupe["nom"].upper() != nom_groupe:
                        new_liste_g.append (groupe)
                
                for membre in liste:
                    num_c = list (membre["groupe"])
                    if num in num_c:
                        new_num = ""
                        for i in range (len (num_c)):
                            if num_c[i] != num:
                                new_num += num_c[i]
                        membre["groupe"] = str (new_num)
                ecriture_csv (f_rep, liste)
                ecriture_csv (f_groupes, new_liste_g)
                print (f"Le groupe {nom} à été supprimé !\n")
                logging.info (f"SUPPRESSION GROUPE: {nom}\n")
                return ""
            os.system ("cls")
            return ""
    os.system ("cls")
    return ""