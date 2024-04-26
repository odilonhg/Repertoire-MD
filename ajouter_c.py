from pickle import *
import os

def ajouter_c():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
    
    else:
        
        dico = {}

    dico[0] = {'nom': ('MESNAGE', 'Dylan'), 'num': '', 'anniv': '13-10-2007','anniv2': '13 Octobre 2007', 'favori': 'True'}
    
    nom = input ('\nSaisir le nom du contact : ').upper()
    prenom = input ('Saisir le prénom du contact : ').capitalize()
    cle = (nom, prenom)
    
    num_contact = input ('Saisir le numéro de téléphone du contact : ')
    
    jour_contact = input ('Saisir le jour de naissance : ')
    mois_contact = int (input ('Saisir le mois de naissance : '))
    annee_contact = input ('Saisir l\'année de naissance : ')
    
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
    
    anniv_contact = (f'{jour_contact}-{mois_nombre[mois_contact]}-{annee_contact}')
    anniv2_contact = (f'{jour_contact} {mois_lettre[mois_contact]} {annee_contact}')
    
    favori = input (f'\nVoulez-vous que le contact {nom} {prenom} soit dans vos favoris ? ').upper()
    print ()
    
    if favori == 'OUI':
        favori = 'True'
    else:
        favori = 'False'
    
    dico[len(dico.keys())] = {f'nom': cle, 'num': num_contact, 'anniv': anniv_contact, 'anniv2': anniv2_contact, 'favori': favori}
    
    rep = open ('MD_repertoire', 'wb')
    dump (dico, rep)
    rep.close()
    
    print (f'Le contact {nom} {prenom} à été crée !\n')
    
    from choix import choix
    return choix()