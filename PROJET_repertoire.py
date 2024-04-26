from pickle import *

def ajoute():
    rep = open ('MD_repertoire','rb')
    repertoire = load(rep)
    rep.close()
    
    nom = input ('\nSaisir le nom du contact : ').upper()
    prenom = input ('Saisir le prénom du contact : ').capitalize()
    cle = (nom,prenom)

    num = input ('Saisir le numéro de téléphone du contact : ')
    repertoire[cle] = num
    
    rep = open ('MD_repertoire','wb')
    dump (repertoire,rep)
    rep.close()
    return choix()

def recherche():
    rep = open ("MD_repertoire",'rb')
    dico_recherche = load(rep)
    rep.close()
#     print(dico_recherche)
    contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
    for name in dico_recherche.keys():
#         print(name)
        if contact_recherche.lower() == name[0].lower():
            print('')
            print(name, ':', dico_recherche[name])
            print('')
        elif contact_recherche.lower() == name[1].lower():
            print('')
            print(name, ':', dico_recherche[name])
            print('')
    return choix()    

def affiche():
    rep = open ("MD_repertoire",'rb')
    repertoire = load(rep)
    rep.close()
    
    if len (repertoire.keys()) >= 1:
        print ('\nListe des contacts :')
        for name, num in repertoire.items():
            print (f'{name} : {num}')
    else:
        return print ('\nAucun contact trouvé.'),choix()
        
    return choix()

def ajoute_fav():
    rep = open ("MD_repertoire", 'rb')
    repertoire = load(rep)
    rep.close()
    print('')
    rep_fav = open ("MD_repertoire_fav", "rb")
    repertoire_fav = load(rep_fav)
    rep_fav.close()

    contact_recherche = input ('Donnez le nom ou le prénom du contact à ajouter aux favoris : ')
    
    for name in repertoire.keys():
        if contact_recherche.lower() == name[0].lower():
            if name in repertoire_fav.keys():
                return print ('\nContact déjà en favori'),options()
            repertoire_fav[name] = repertoire[name]
            rep_fav = open ("MD_repertoire_fav", "wb")
            dump (repertoire_fav,rep_fav)
            rep_fav.close()
            return print (f'\nLe contact {name} a été ajouté aux favoris !'),options()
        elif contact_recherche.lower() == name[1].lower():
            if name in repertoire_fav.keys():
                return print ('\nContact déjà en favori'),options()
            repertoire_fav[name] = repertoire[name]
            rep_fav = open ("MD_repertoire_fav", "wb")
            dump (repertoire_fav,rep_fav)
            rep_fav.close()
            return print (f'\nLe contact {name} a été ajouté aux favoris !'),options()
    
    return print ('\nContact inexistant !'),options()

def affiche_fav():
    rep = open ("MD_repertoire_fav",'rb')
    repertoire = load(rep)
    rep.close()
    
    if len (repertoire.keys()) >= 1:
        print ('\nListe des contacts favoris :')
        for name, num in repertoire.items():
            print (f'{name} : {num}')
    else:
        return print ('\nAucun contact ajouté en favori.'),options()
        
    return options()

def supprimer_fav():
    rep_fav = open ("MD_repertoire_fav", "rb")
    repertoire_fav = load(rep_fav)
    rep_fav.close()
    print('')
    contact_recherche = input ('Donnez le nom ou le prénom du contact à supprimer de vos favoris : ')
    
    for name in repertoire_fav.keys():
        if contact_recherche.lower() == name[0].lower():
            if name in repertoire_fav.keys():
                del repertoire_fav[name]
                rep_fav = open ("MD_repertoire_fav", "wb")
                dump(repertoire_fav,rep_fav)
                rep_fav.close()
                return print (f'\nLe contact {name} à été retiré des favoris !'),options()
        elif contact_recherche.lower() == name[1].lower():
            if name in repertoire_fav.keys():
                del repertoire_fav[name]
                rep_fav = open ("MD_repertoire_fav", "wb")
                dump (repertoire_fav,rep_fav)
                rep_fav.close()
                return print (f'\nLe contact {name} à été retiré des favoris !'),options()
            
    return print ("\nLe contact est inexistant ou n'est pas dans les favoris"),options()

def supprimer():
    print ('\nATTENTION, cette action est irréversible !')
    avertissement = input ('\nTappez "oui" pour confirmer ou "non" pour annuler : ')
    while avertissement != 'oui' and avertissement != 'non':
        avertissement = input ('\nRéponse invalide. Veuillez taper "oui" pour confirmer ou "non" pour annuler : ')
    if avertissement == 'non':
        return print ('\nAction annulée'),options()
    elif avertissement == 'oui':
        rep = open ('MD_repertoire','rb')
        repertoire = load(rep)
        rep.close()
    
        contact = input ('\nDonnez le nom ou le prénom du contact à supprimer : ')
        for name in repertoire.keys():
            if contact.lower() == name[0].lower():
                if name in repertoire.keys():
                    del repertoire[name]
                    rep = open ('MD_repertoire','wb')
                    dump (repertoire,rep)
                    rep.close()
                    return print (f'\nLe contact {name} a été supprimé !'),options()
            if contact.lower() == name[1].lower():
                if name in repertoire.keys():
                    del repertoire[name]
                    rep = open ('MD_repertoire','wb')
                    dump (repertoire,rep)
                    rep.close()
                    return print (f'\nLe contact {name} a été supprimé !'),options()
        return print ("\nLe contact est inexistant !"),options()

def modifier():
    rep = open ('MD_repertoire','rb')
    repertoire = load(rep)
    rep.close()
    
    print('')
    contact = input ('Donnez le nom ou le prénom du contact à modifier : ')
    for name in repertoire.keys():
        if contact.lower() == name[0].lower():
            if name in repertoire.keys():
                print('')
                nouveau_num = input (f'Entrez un nouveau numéro de téléphone pour {name} : ')
                repertoire[name]=nouveau_num
                rep = open ('MD_repertoire','wb')
                dump(repertoire,rep)
                rep.close()
                return print ('\nLe numéro du contact a été modifié !'),options()
        elif contact.lower() == name[1].lower():
            if name in repertoire.keys():
                print('')
                nouveau_num = input (f'Entrez un nouveau numéro de téléphone pour {name} : ')
                repertoire[name] = nouveau_num
                rep = open ('MD_repertoire','wb')
                dump (repertoire,rep)
                rep.close()
                return print ('\nLe numéro du contact a été modifié !'),options()
    return print ('\nContact inexistant'),options()
                
def choix():
    print ('\n1-Rechercher un contact')
    print ('2-Ajouter un contact')
    print ('3-Afficher les contacts')
    print ('4-Options Spéciales')
    print ('5-Quitter')
    choice = input ("Choix : ")
    if choice == "5":
        return ""
    elif choice == "1":
        return recherche()
    elif choice == "2":
        return ajoute()
    elif choice == '3':
        return affiche()
    elif choice == "4":
        return options()
    else:
        print ('\nChoix impossible')
        return choix()
    
def options():
    print ('\n1-Ajouter un favori')
    print ('2-Afficher les favoris')
    print ('3-Supprimer un favori')
    print ('4-Modifier un contact')
    print ('5-Supprimer un contact')
    print ('6-Retour')
    choice=input('Choix : ')
    if choice == "6":
        return choix()
    elif choice == '1':
        return ajoute_fav()
    elif choice == '2':
        return affiche_fav()
    elif choice == '3':
        return supprimer_fav()
    elif choice == '4':
        return modifier()
    elif choice == '5':
        return supprimer()
    else:
        print ('\nChoix impossible\n')
        return options()
choix()