from lecture_ecriture import lecture_csv
import logging
import os

f_rep = "data_contacts.csv"
f_groupes = "data_groupes.csv"

def g_rechercher ():
    liste = lecture_csv (f_rep)
    liste_g = lecture_csv (f_groupes)
    nom_groupe = input ("Saisir le nom ou le numéro du groupe à trouver : ").upper ()
    logging.info (f"RECHERCHE GROUPE: {nom_groupe}\n")
    
    os.system ("cls")
    print ("- Groupe/s Trouvé/s -")
    
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