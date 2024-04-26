import os
from pickle import *

def ajoute():
    
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
    
    print (f'\nLe contact {nom} {prenom} à été crée !\n')
    
    return choix()


def recherche():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
        
        contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
        
        for i in range(len(dico.keys())):
        
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
        
            if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                print(f"\n|   {nom} {prenom}")
                print(f"| - Numéro de téléphone : {dico[i]['num']}")
                print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
                
        return choix()

    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()

def affiche():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
        
        print ('\n--- Les Contacts ---')
        print ('* = Contact Favori\n')
        
        for i in range (len(dico.keys())):
            
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            favori = dico[i]['favori']
            
            if favori == 'True':
                print(f"| * {nom} {prenom}")
                print(f"| - Numéro de téléphone : {dico[i]['num']}")
                print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
            
            elif favori == 'False':
                print(f"|  {nom} {prenom}")
                print(f"| - Numéro de téléphone : {dico[i]['num']}")
                print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
            
    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()
        
    return choix()

def ajoute_fav():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()

        contact_recherche = input ('\nDonnez le nom ou le prénom du contact à ajouter aux favoris : ')
        
        for i in range (len(dico.keys())):
            
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            
            if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                dico[i]['favori'] = 'True'
                
                rep = open ('MD_repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {nom} {prenom} à été ajouté aux favoris !\n')
                return choix()
        
    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()

def affiche_fav():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
            
        print ('\n--- Les Contacts Favoris ---\n')
        
        for i in range (len(dico.keys())):
        
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            favori = dico[i]['favori']
            
            if favori == 'True':
                print(f"|   {nom} {prenom}")
                print(f"| - Numéro de téléphone : {dico[i]['num']}")
                print(f"| - Anniversaire : {dico[i]['anniv2']}\n")
        
        return choix()
    
    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()

def supprimer_fav():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
        
        contact_recherche = input('\nDonnez le nom ou le prénom du contact à supprimer de vos favoris : ')
        
        for i in range (len(dico.keys())):
            
            nom = dico[i]['nom'][0]
            prenom = dico[i]['nom'][1]
            
            if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                dico[i]['favori'] = 'False'
                
                rep = open ('MD_repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {nom} {prenom} à été supprimé des favoris !\n')
                return choix()
    
    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()

def supprimer():
    
    print ('\nATTENTION, cette action est irréversible !')
    
    avertissement = input ('\nTappez "oui" pour confirmer ou "non" pour annuler : ')
    
    while avertissement != 'oui' and avertissement != 'non':
        avertissement = input ('\nRéponse invalide. Veuillez taper "oui" pour confirmer ou "non" pour annuler : ')
        
    if avertissement == 'non':
        print ('\nAction annulée\n')
        return choix()
    
    elif avertissement=='oui':
        
        fichier_repertoire = 'MD_repertoire'

        if os.path.exists (fichier_repertoire):
        
            rep = open ('MD_repertoire', 'rb')
            dico = load(rep)
            rep.close()
    
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact à supprimer : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
            
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                    
                    del dico[i]
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été supprimé !\n')
                    return choix()
        
        else:
        
            print ('\nAucun contact trouvé.\n')
            return choix()

def modifier():
    
    fichier_repertoire = 'MD_repertoire'

    if os.path.exists (fichier_repertoire):
        
        rep = open ('MD_repertoire', 'rb')
        dico = load(rep)
        rep.close()
    
        print ('\n--- Modification de Contact ---\n')
        print ('1. Modifier le nom')
        print ('2. Modifier le prénom')
        print ('3. Modifier le numéro de téléphone')
        print ('4. Modifier la date de naissance\n')
    
        choice = input ('Choix : ')
    
        def modifier_nom():
        
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
        
            for i in range(len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
        
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
            
                    nom = input (f'\nSaisir le nouveau nom de {nom} {prenom} : ').upper()
                    prenom = dico[i]['nom'][1]
                    cle = (nom, prenom)
                    num = dico[i]['num']
                    anniv = dico[i]['anniv']
                    anniv2 = dico[i]['anniv2']
                    favori = dico[i]['favori']
                
                    dico[i] = {'nom': cle, 'num': num, 'anniv': anniv, 'anniv2': anniv2, 'favori': favori}
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été modifié !\n')
                    return choix()
        
            else:
            
                print ('\nAucun contact trouvé.\n')
                return choix()
    
        def modifier_prenom():
            
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
                
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                    nom = dico[i]['nom'][0]
                    prenom = input (f'\nSaisir le nouveau prénom de {nom} {prenom} : ').capitalize()
                    cle = (nom, prenom)
                    num = dico[i]['num']
                    anniv = dico[i]['anniv']
                    anniv2 = dico[i]['anniv2']
                    favori = dico[i]['favori']
                    
                    dico[i] = {'nom': cle, 'num': num, 'anniv': anniv, 'anniv2': anniv2, 'favori': favori}
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été modifié !\n')
                    return choix()
            
            else:
            
                print ('\nAucun contact trouvé.\n')
                return choix()
            
        def modifier_num():
            
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
                
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                    cle = (nom, prenom)
                    num = input (f'\nSaisir le nouveau numéro de téléphone de {nom} {prenom} : ')
                    anniv = dico[i]['anniv']
                    anniv2 = dico[i]['anniv2']
                    favori = dico[i]['favori']
                    
                    dico[i] = {'nom': cle, 'num': num, 'anniv': anniv, 'anniv2': anniv2, 'favori': favori}
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été modifié !\n')
                    return choix()
                
            else:
                
                print ('\nAucun contact trouvé.\n')
                return choix()
            
        def modifier_anniv():
            
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
                
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                    cle = (nom, prenom)
                    num = dico[i]['num']
                    
                    jour_contact = input ('\nSaisir le jour de naissance : ')
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
        
                    anniv = (f'{jour_contact}-{mois_nombre[mois_contact]}-{annee_contact}')
                    anniv2 = (f'{jour_contact} {mois_lettre[mois_contact]} {annee_contact}')
                    favori = dico[i]['favori']
                    
                    dico[i] = {'nom': cle, 'num': num, 'anniv': anniv, 'anniv2': anniv2, 'favori': favori}
                    
                    rep = open ('MD_repertoire', 'wb')
                    dump (dico, rep)
                    rep.close()
                    
                    print (f'\nLe contact {nom} {prenom} a été modifié !\n')
                    return choix()
                
            else:
            
                print ('\nAucun contact trouvé.\n')
                return choix()
            
        if choice == '1':
            return modifier_nom()
        
        elif choice == '2':
            return modifier_prenom()
        
        elif choice == '3':
            return modifier_num()
            
        elif choice == '4':
            return modifier_anniv()
        
        else:
            print ('\nChoix Impossible !\n')
            return choix()

    else:
        
        print ('\nAucun contact trouvé.\n')
        return choix()

def choix():
    print ('--- Le Répertoire ---\n')
    print ('1. Ajouter un contact')
    print ('2. Rechercher un contact')
    print ('3. Afficher les contacts')
    print ('4. Ajouter un favori')
    print ('5. Afficher les favoris')
    print ('6. Supprimer un favori')
    print ('7. Supprimer un contact')
    print ('8. Modifier un contact')
    print ('9. Quitter\n')
    
    choice = input ("Choix : ")
    
    if choice == '1':
        return ajoute()
    
    elif choice == '2':
        return recherche()
    
    elif choice == '3':
        return affiche()
    
    elif choice == '4':
        return ajoute_fav()
    
    elif choice == '5':
        return affiche_fav()
    
    elif choice == '6':
        return supprimer_fav()
    
    elif choice == '7':
        return supprimer()
    
    elif choice == '8':
        return modifier()
    
    elif choice == '9':
        return ''
    
    else:
        print ('\nChoix Impossible !\n')
        return choix()

choix()

# dico[len(dico.keys())] = {'nom': '', 'num': '', 'anniv': '', 'anniv2': '', 'favori': ''}
# for name, num, anniv, anniv2, favori in dico.values():