from pickle import *
import logging

dico = {}
dico [0] = {}
dico [0]['nom'] = 'MESNAGE'
dico [0]['prenom'] = 'Dylan'
dico [0]['jour'] = '13'
dico [0]['mois'] = '10'
dico [0]['mois2'] = 'Octobre'
dico [0]['annee'] = '2007'
dico [0]['num'] = '0665218476'
dico [0]['email'] = 'dmesnage.hg@gmail.com'
dico [0]['favori'] = True
dico [0]['note'] = 'C\'est moi, le développeur de ce répertoire !'

logging.info(f'Le contact MESNAGE Dylan a été crée\n')

nom = ''
prenom = ''
jour = ''
mois_c = ''
mois = ''
mois2 = ''
annee = ''
num = ''
email = ''
favori = True

fichier_repertoire = 'MD_repertoire'

def depart():
    
    print ('Bienvenue dans le MD_Répertoire !\nCréons votre contact dès maintenant !')
        
    return choix()

def choix():
    
    global nom, prenom, jour, mois_c, annee, num, email, favori
    
    print ('\nQue souhaitez-vous ajouter ?\n')
    
    print ('1. Le nom')
    print ('2. Le prénom')
    print ('3. La date de naissance')
    print ('4. Le numéro de téléphone')
    print ('5. l\'adresse email')
    print ('6. Finir le contact !\n')
    
    choice = input ('Choix : ')
    
    if choice == '1' and nom == '':
        return ajouter_nom()
    elif choice == '1' and nom != '':
        print('\nNom déjà renseigné !')
        return choix()
    
    elif choice == '2' and prenom == '':
        return ajouter_prenom()
    elif choice == '2' and prenom != '':
        print('\nPrénom déjà renseigné !')
        return choix()
    
    elif choice == '3' and jour == '':
        return ajouter_date()
    elif choice == '3' and jour != '':
        print('\nDate de naissance déjà renseignée !')
        return choix()
    
    elif choice == '4' and num == '':
        return ajouter_num()
    elif choice == '4' and num != '':
        print('\nNuméro de téléphone déjà renseigné !')
        return choix()
    
    elif choice == '5' and email == '':
        return ajouter_email()
    elif choice == '5' and email != '':
        print('\nAdresse email déjà renseignée !')
        return choix()
    
    elif choice == '6':
        return fin()
    
    else:
        print('\nChoix impossible !\n')
        return choix()

def ajouter_nom():
    global nom
    nom = input ('\nBien, donnez moi votre nom de famille : ').upper()
    return choix()

def ajouter_prenom():
    global prenom
    prenom = input ('\nBien, donnez moi votre prénom : ').capitalize()
    return choix()

def ajouter_date():
    global jour, mois_c, mois, mois2, annee
    
    mois_nombre = {
        1: '01',
        2: '02',
        3: '03',
        4: '04',
        5: '05',
        6: '06',
        7: '07',
        8: '08',
        9: '09',
        10: '10',
        11: '11',
        12: '12'
    }
    
    mois_lettre = {
        1: 'Janvier',
        2: 'Février',
        3: 'Mars',
        4: 'Avril',
        5: 'Mai',
        6: 'Juin',
        7: 'Juillet',
        8: 'Août',
        9: 'Septembre',
        10: 'Octobre',
        11: 'Novembre',
        12: 'Décembre'
    }
    
    jour = input ('\nBien, donnez moi votre jour de naissance : ')
    mois_c = int (input ('Maintenant, donnez moi votre mois de naissance : '))
    mois = mois_nombre[mois_c]
    mois2 = mois_lettre[mois_c]
    annee = input ('Enfin, donnez moi votre année de naissance : ')
    return choix()

def ajouter_num():
    global num
    num = input ('\nBien, donnez moi votre numéro de téléphone : ')
    return choix()

def ajouter_email():
    global email
    email = input ('\nBien, donnez moi votre adresse email : ')
    return choix()

def fin():
    
    global nom, prenom, jour, mois_c, mois, mois2, annee, num, email, favori
    
    dico[len(dico.keys())] = {}
    
    if nom == '':
        nom = input ('\nNom obligatoire ! Renseignez votre nom de famille ici : ').upper()
        return fin()
    if prenom == '':
        prenom = input ('\nPrénom obligatoire ! Renseignez votre prénom ici : ').capitalize()
        return fin()
    
    dico[max(dico.keys())]['nom'] = nom
    dico[max(dico.keys())]['prenom'] = prenom
    
    if jour != '':
        
        dico[max(dico.keys())]['jour'] = jour
        
        if mois_c == '':
            dico[max(dico.keys())]['mois'] = 'MM'
            dico[max(dico.keys())]['mois2'] = 'MM'
        elif mois_c != '':    
            dico[max(dico.keys())]['mois'] = mois
            dico[max(dico.keys())]['mois2'] = mois2
        
        if annee == '':
            dico[max(dico.keys())]['annee'] = 'AAAA'
        elif annee != '':
            dico[max(dico.keys())]['annee'] = annee
            
    if num != '':
        dico[max(dico.keys())]['num'] = num
    if email != '':
        dico[max(dico.keys())]['email'] = email
    
    dico[max(dico.keys())]['favori'] = favori
    
    rep = open(fichier_repertoire, 'wb')
    dump (dico, rep)
    rep.close()
    
    print ('\nBien, bon voyage dans notre répertoire !\n')
    logging.info(f'Le contact {nom} {prenom} a été crée\n')
    from choix import choix
    return choix()