from pickle import *
import logging

fichier_repertoire = 'MD_repertoire'

rep = open ('MD_repertoire', 'rb')
dico = load(rep)
rep.close()

nom = ''
prenom = ''
jour = ''
mois_c = ''
mois = ''
mois2 = ''
annee = ''
num = ''
email = ''
favori = False
    
def ajouter_c():
    
    global nom, prenom, jour, mois_c, mois, mois2, annee, num, email, favori
    
    print ('\n--- Créer un Contact ---\n')
    
    print ('1. Le nom')
    print ('2. Le prénom')
    print ('3. La date de naissance')
    print ('4. Le numéro de téléphone')
    print ('5. l\'adresse email')
    print ('6. Finir le contact !\n')
    
    choice = input ('Choix : ')
    
    if choice == '1' and nom == '':
        nom = input ('\nSaisir le nom de famille : ').upper()
        return ajouter_c()
    elif choice == '1' and nom != '':
        print('\nNom déjà renseigné !')
        return ajouter_c()
    
    elif choice == '2' and prenom == '':
        prenom = input ('\nSaisir le prénom : ').capitalize()
        return ajouter_c()
    elif choice == '2' and prenom != '':
        print('\nPrénom déjà renseigné !')
        return ajouter_c()
    
    elif choice == '3' and jour == '':
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
    
        jour = input ('\nSaisir le jour de naissance : ')
        mois_c = int (input ('Saisir le mois de naissance : '))
        mois = mois_nombre[mois_c]
        mois2 = mois_lettre[mois_c]
        annee = input ('Saisir l\'année de naissance : ')
        return ajouter_c()
    elif choice == '3' and jour != '':
        print('\nDate de naissance déjà renseignée !')
        return ajouter_c()
    
    elif choice == '4' and num == '':
        num = input ('\nSaisir le numéro de téléphone : ')
        return ajouter_c()
    elif choice == '4' and num != '':
        print('\nNuméro de téléphone déjà renseigné !')
        return ajouter_c()
    
    elif choice == '5' and email == '':
        email = input ('\nSaisir l\'adresse email : ')
        return ajouter_c()
    elif choice == '5' and email != '':
        print('\nAdresse email déjà renseignée !')
        return ajouter_c()
    
    elif choice == '6':
        return fin_c()
    
    else:
        print('\nChoix impossible !\n')
        return ajouter_c()

def fin_c():
    
    global nom, prenom, jour, mois_c, mois, mois2, annee, num, email, favori, fichier_repertoire, dico
    
    dico[len(dico.keys())] = {}
    
    if nom == '':
        nom = input ('\nNom obligatoire ! Renseignez votre nom de famille ici : ').upper()
        return fin_c()
    if prenom == '':
        prenom = input ('\nPrénom obligatoire ! Renseignez votre prénom ici : ').capitalize()
        return fin_c()
    
    dico[max(dico.keys())]['nom'] = nom
    dico[max(dico.keys())]['prenom'] = prenom
    
    choice = input ('\nVoulez-vous ajouter ce contact en favori ? ').upper()
    
    if choice == 'OUI':
        favori = True
    
    if jour != '':
        dico[max(dico.keys())]['jour'] = jour
    
    if mois_c != '':    
        dico[max(dico.keys())]['mois'] = mois
        dico[max(dico.keys())]['mois2'] = mois2
        
    if annee != '':
        dico[max(dico.keys())]['annee'] = annee
            
    if num != '':
        dico[max(dico.keys())]['num'] = num
        
    if email != '':
        dico[max(dico.keys())]['email'] = email
    
    dico[max(dico.keys())]['favori'] = favori
    
    rep = open(fichier_repertoire, 'wb')
    dump (dico, rep)
    rep.close()
    
    favori = False
    
    print (f'\nLe contact {nom} {prenom} a été crée !')
    logging.info(f'NOUVEAU CONTACT: {nom} {prenom}\n')
    
    nom = ''
    prenom = ''
    jour = ''
    mois_c = ''
    mois = ''
    mois2 = ''
    annee = ''
    num = ''
    email = ''
    
    from a_contacts.choix_c import choix_c
    return choix_c()