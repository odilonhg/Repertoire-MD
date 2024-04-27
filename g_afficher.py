from lecture_ecriture import lecture_csv
import logging
import os

f_rep = "data_contacts.csv"
f_groupes = "data_groupes.csv"

def g_afficher ():
    logging.info (f"AFFICHE: GROUPES\n")
    print ("- Les Groupes -")
    liste = lecture_csv (f_rep)
    liste_g = lecture_csv (f_groupes)
    
    for groupe in liste_g:
        
        nom = groupe["nom"]
        num = groupe["num"]
        nbr_mbr = groupe["nbr_mbr"]
            
        print (f"\n| {num}. {nom}")
        print (f"|    Membres : {nbr_mbr}/100")
        
        for membre in liste:
            membre_num = list (membre["groupe"])
            membre_nom = membre["nom"]
            membre_prenom = membre["prenom"]
            membre_num_tel = membre["num"]
            membre_email = membre["email"]
            membre_jour = membre["jour"]
            membre_mois = membre["mois"]
            membre_annee = membre["annee"]
            
            if num in membre_num:
                
                print (f"|")
                print (f"|    {membre_nom} {membre_prenom}")
                if membre_jour != "":
                    print (f"|    {membre_jour}/{membre_mois}/{membre_annee}")
                if membre_num_tel != "":
                    print (f"|    {membre_num_tel}")
                if membre_email != "":
                    print (f"|    {membre_email}")
    
    print ()
    return ""