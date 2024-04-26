import logging
import csv

def ecriture(rep,liste,delimiter=";"):
    
    with open (rep,"w") as csvfile:
        ligneDesc = ";".join(liste[0].keys()) + "\n"
        csvfile.write (ligneDesc)
        
        for cle in range(len(liste)):
            ligne = ";".join (liste[cle].values()) + "\n"
            csvfile.write (ligne)

liste = [{"nom": "MESNAGE", "prenom": "Dylan", "jour": "13", "mois": "10", "annee": "2007", "num": "0665218476", "email": "dmesnage.hg@gmail.com", "favori": "True"},
         {"nom": "GORLAS", "prenom": "Maxime", "jour": "", "mois": "", "annee": "", "num": "", "email": "", "favori": "True"}]

nom = ""
prenom = ""
jour = ""
mois = ""
annee = ""
num = ""
email = ""
favori = "True"

f_rep = "Repertoire MD.csv"

def depart():
    
    print ("Bienvenue dans le MD_Répertoire !\nCréons votre contact dès maintenant !")
        
    return d_choix()

def d_choix():
    
    global nom, prenom, jour, mois, annee, num, email, favori
    
    print ("\nQue souhaitez-vous ajouter ?\n")
    
    print ("1. Le nom")
    print ("2. Le prénom")
    print ("3. La date de naissance")
    print ("4. Le numéro de téléphone")
    print ("5. L'adresse email")
    print ("6. Finir le contact !\n")
    
    choice = input ("Choix : ")
    
    if choice == '1' and nom == '':
        return ajouter_nom()
    elif choice == '1' and nom != '':
        print('\nNom déjà renseigné !')
        return d_choix()
    
    elif choice == '2' and prenom == '':
        return ajouter_prenom()
    elif choice == '2' and prenom != '':
        print('\nPrénom déjà renseigné !')
        return d_choix()
    
    elif choice == '3' and jour == '':
        return ajouter_date()
    elif choice == '3' and jour != '':
        print('\nDate de naissance déjà renseignée !')
        return d_choix()
    
    elif choice == '4' and num == '':
        return ajouter_num()
    elif choice == '4' and num != '':
        print('\nNuméro de téléphone déjà renseigné !')
        return d_choix()
    
    elif choice == '5' and email == '':
        return ajouter_email()
    elif choice == '5' and email != '':
        print('\nAdresse email déjà renseignée !')
        return d_choix()
    
    elif choice == '6':
        return fin()
    
    else:
        print('\nChoix impossible !\n')
        return d_choix()

def ajouter_nom():
    global nom
    nom = input ('\nRenseignez votre nom de famille : ').upper()
    return d_choix()

def ajouter_prenom():
    global prenom
    prenom = input ('\nRenseignez votre prénom : ').capitalize()
    return d_choix()

def ajouter_date():
    global jour, mois_c, mois, mois2, annee
    
    jour = input ('\nRenseignez votre jour de naissance (de 1 à 31) : ')
    mois = input ('Renseignez votre mois de naissance (de 1 à 12) : ')
    annee = input ('Renseignez votre année de naissance : ')
    return d_choix()

def ajouter_num():
    global num
    num = input ('\nRenseignez votre numéro de téléphone (10 caractères) : ')
    return d_choix()

def ajouter_email():
    global email
    email = input ('\nRenseignez votre adresse email : ')
    return d_choix()

def fin():
    
    global nom, prenom, jour, mois_c, mois, mois2, annee, num, email, favori
    
    if nom == '':
        nom = input ('\nNom obligatoire ! Renseignez votre nom de famille ici : ').upper()
        return fin()
    if prenom == '':
        prenom = input ('\nPrénom obligatoire ! Renseignez votre prénom ici : ').capitalize()
        return fin()
    
    liste.append ({'nom': nom, 'prenom': prenom, 'jour': jour, 'mois': mois, 'annee': annee, 'num': num, 'email': email, 'favori': favori})
    
    ecriture(f_rep, liste) 
    
    print ("\nBien, bon voyage dans notre répertoire !\n")
    logging.info(f"NOUVEAU CONTACT: {nom} {prenom}\n")
    from choix import choix
    return choix()