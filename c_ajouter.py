from lecture_ecriture import *
import logging
import csv
import os

f_rep = "data_contacts.csv"

nom = ""
prenom = ""
jour = ""
mois = ""
annee = ""
num = ""
email = ""

liste = lecture_csv (f_rep)

def c_ajouter ():
    global nom, prenom, jour, mois, annee, num, email
    
    print ("- Ajouter un Contact -\n")
    
    print ("0. Annuler !")
    print ("1. Le nom")
    print ("2. Le prénom")
    print ("3. La date de naissance")
    print ("4. Le numéro de téléphone")
    print ("5. l\'adresse email")
    print ("6. Finir le contact !\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            return ""
        
        case "1":
            if nom == "":
                nom = input ("\nRenseigner le nom de famille du contact : ").upper()
                os.system ("cls")
                return c_ajouter()
            else:
                os.system ("cls")
                return c_ajouter()
        
        case "2":
            if prenom == "":
                prenom = input ("\nRenseigner le prénom du contact : ").capitalize()
                os.system ("cls")
                return c_ajouter()
            else:
                os.system ("cls")
                return c_ajouter()
        
        case "3":
            if jour == "":
                jour = input ("\nRenseigner le jour de naissance du contact (de 1 à 31) : ")
                mois = input ("\nRenseigner le mois de naissance du contact (de 1 à 12) : ")
                annee = input ("\nRenseigner votre année de naissance : ")
                os.system ("cls")
                return c_ajouter()
            else:
                os.system ("cls")
                return c_ajouter()
            
        case "4":
            if num == "":
                num = input ("\nRenseignez le numéro de téléphone du contact (10 caractères) : ")
                os.system ("cls")
                return c_ajouter()
            else:
                os.system ("cls")
                return c_ajouter()
        
        case "5":
            if email == '':
                email = input ("\nRenseigner l'adresse email du contact : ")
                os.system ("cls")
                return c_ajouter()
            else:
                os.system ("cls")
                return c_ajouter()
        
        case "6":
            return fin()
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        
        case _:
            os.system ("cls")
            print ("Choix impossible...\n")
            return c_ajouter()

def fin():
    global nom, prenom, jour, mois, annee, num, email, liste
    
    if nom == "":
        nom = input ('\nNom obligatoire ! Renseignez votre nom de famille ici : ').upper()
        return fin()
    if prenom == "":
        prenom = input ('\nPrénom obligatoire ! Renseignez votre prénom ici : ').capitalize()
        return fin()
    
    choice = input ("\nVoulez-vous que ce contact soit en favori ? ").upper()
    
    if choice == "OUI":
        favori = "True"
    else:
        favori = "False"
        
    c_new = {"nom": nom, "prenom": prenom, "jour": jour, "mois": mois, "annee": annee, "num": num, "email": email, "favori": favori, "groupe": ""}
    
    liste.append (c_new)
    
    ecriture_csv (f_rep, liste)
    
    os.system ("cls")
    print (f"Le contact {nom} {prenom} a été crée !\n")
    logging.info(f"NOUVEAU CONTACT: {nom} {prenom}\n")
    
    return ""