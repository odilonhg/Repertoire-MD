from pickle import *
import os

def modifier_c():
    
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
                    from choix import choix
                    return choix()
        
            else:
            
                print ('\nAucun contact trouvé.\n')
                from choix import choix
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
                    from choix import choix
                    return choix()
            
            else:
            
                print ('\nAucun contact trouvé.\n')
                from choix import choix
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
                    from choix import choix
                    return choix()
                
            else:
                
                print ('\nAucun contact trouvé.\n')
                from choix import choix
                return choix()
            
        def modifier_anniv():
            
            contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
            
            for i in range (len(dico.keys())):
                
                nom = dico[i]['nom'][0]
                prenom = dico[i]['nom'][1]
                
                if contact_recherche.lower() == nom.lower() or contact_recherche.lower() == prenom.lower():
                
                    cle = (nom, prenom)
                    num = dico[i]['num']
                    
                    jour_contact = input (f'\nSaisir le jour de naissance de {nom} {prenom} : ')
                    mois_contact = int (input ('Saisir son mois de naissance : '))
                    annee_contact = input ('Saisir son année de naissance : ')
        
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
                    from choix import choix
                    return choix()
                
            else:
            
                print ('\nAucun contact trouvé.\n')
                from choix import choix
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
            from choix import choix
            return choix()

    else:
        
        print ('\nAucun contact trouvé.\n')
        from choix import choix
        return choix()