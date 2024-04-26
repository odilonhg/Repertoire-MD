from pickle import *
import logging

fichier_repertoire = 'MD_repertoire'

rep = open ('MD_repertoire', 'rb')
dico = load(rep)
rep.close()

def modifier_c():
    
    global fichier_repertoire, dico
    
    print ('\n--- Modification de Contact ---\n')
    print ('1. Modifier le nom')
    print ('2. Modifier le prénom')
    print ('3. Modifier la date de naissance')
    print ('4. Modifier le numéro de téléphone')
    print ('5. Modifier l\'adresse email')
    print ('6. Retour à la Gestion des Contacts\n')
    
    choice = input ('Choix : ')
    
    if choice == '6':
        from a_contacts.choix_c import choix_c
        return choix_c()
        
    contact = input ('\nDonnez le nom ou le prénom du contact : ').upper()
        
    for indice, contacts in dico.items():
            
        nom = contacts.get ('nom').upper()
        prenom = contacts.get ('prenom').upper()
        
        jour = contacts.get ('jour', None)
        mois = contacts.get ('mois', None)
        mois2 = contacts.get ('mois2', None)
        annee = contacts.get ('annee', None)
        num = contacts.get ('num', None)
        email = contacts.get ('email', None)
        favori = contacts.get ('favori', False)
            
        if contact == nom or contact == prenom:
            prenom = contacts.get ('prenom').capitalize()
            
            if choice == '1':
                nom = input (f'\nSaisir le nouveau nom de {nom} {prenom} : ').upper()
            
            elif choice == '2':
                prenom = input (f'\nSaisir le nouveau prénom de {nom} {prenom} : ').capitalize()
            
            elif choice == '3':
                jour = input (f'\nSaisir le jour de naissance de {nom} {prenom} : ')
                mois_c = int (input (f'\nSaisir le mois de naissance de {nom} {prenom} : '))
                annee = input (f'\nSaisir l\'année de naissance de {nom} {prenom} : ')
                
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
                
                mois = mois_nombre[mois_c]
                mois2 = mois_lettre[mois_c]
                
            
            elif choice == '4':
                num = input (f'\nSaisir le nouveau numéro de téléphone de {nom} {prenom} : ')
            
            elif choice == '5':
                email = input (f'\nSaisir la nouvelle adresse email de {nom} {prenom} : ')
            
            else:
                print ('\nChoix impossible !')
                return modifier_c()
            
            choice = 'NONE'
            
            dico[indice] = {'nom': nom, 'prenom': prenom, 'jour': jour, 'mois': mois, 'mois2': mois2, 'annee': annee, 'num': num, 'email': email, 'favori': favori}
            
            rep = open ('MD_repertoire', 'wb')
            dump (dico, rep)
            rep.close()
            
            rep = open ('MD_repertoire', 'rb')
            dico = load(rep)
            rep.close()
            
            print (f'\nLe contact {nom} {prenom} a été modifié !')
            logging.info (f'Modification du contact {nom} {prenom}\n')
            from a_contacts.choix_c import choix_c
            return choix_c()
    
    print ('\nAucun contact trouvé !')
    from a_contacts.choix_c import choix_c
    return choix_c()