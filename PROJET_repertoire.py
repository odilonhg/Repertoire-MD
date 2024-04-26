#ATTENTION, NE PAS PORTER D'ATTENTION PARTICULIERE AUX FONCTIONS la_fin() et la fameuse options_super_mega_speciales_ultra_3000() avant de les avoir essayées !

from pickle import *

def ajoute():
    rep = open ('MD_repertoire', 'rb')
    repertoire = load (rep)
    rep.close()
    
    nom = input ('\nSaisir le nom du contact : ').upper()
    prenom = input ('Saisir le prénom du contact : ').capitalize()
    cle = (nom, prenom)
    num = input ('Saisir le numéro de téléphone du contact : ')
    repertoire[cle] = num
    
    rep = open ('MD_repertoire', 'wb')
    dump (repertoire, rep)
    rep.close()
    return choix()

def recherche():
    rep = open ("MD_repertoire", 'rb')
    dico_recherche = load (rep)
    rep.close()
    contact_recherche = input ('\nDonnez le nom ou le prénom du contact : ')
    for name in dico_recherche.keys():
        if contact_recherche.lower() == name[0].lower():
            print ('')
            print (name, ':', dico_recherche[name])
            print ('')
        elif contact_recherche.lower() == name[1].lower():
            print ('')
            print (name, ':', dico_recherche[name])
            print ('')
    return choix()    

def affiche():
    rep = open ("MD_repertoire", 'rb')
    repertoire = load (rep)
    rep.close()
    
    if len (repertoire.keys()) >= 1:
        print ('\nListe des contacts :')
        for name, num in repertoire.items():
            print (f'{name} : {num}')
    else:
        return print ('\nAucun contact trouvé.'), choix()
        
    return choix()

def ajoute_fav():
    rep = open ("MD_repertoire", 'rb')
    repertoire = load (rep)
    rep.close()
    print ('')
    rep_fav = open ("MD_repertoire_fav", "rb")
    repertoire_fav = load (rep_fav)
    rep_fav.close()

    contact_recherche = input ('Donnez le nom ou le prénom du contact à ajouter aux favoris : ')
    
    for name in repertoire.keys():
        if contact_recherche.lower() == name[0].lower():
            if name in repertoire_fav.keys():
                return print ('\nContact déjà en favori'), options()
            repertoire_fav[name] = repertoire[name]
            rep_fav = open("MD_repertoire_fav", "wb")
            dump (repertoire_fav, rep_fav)
            rep_fav.close()
            return print (f'\nLe contact {name} a été ajouté aux favoris !'), options()
        elif contact_recherche.lower() == name[1].lower():
            if name in repertoire_fav.keys():
                return print ('\nContact déjà en favori'), options()
            repertoire_fav[name] = repertoire[name]
            rep_fav = open ("MD_repertoire_fav", "wb")
            dump (repertoire_fav, rep_fav)
            rep_fav.close()
            return print (f'\nLe contact {name} a été ajouté aux favoris !'), options()
    
    return print ('\nContact inexistant !'), options()

def affiche_fav():
    rep = open ("MD_repertoire_fav", 'rb')
    repertoire = load (rep)
    rep.close()
    
    if len(repertoire.keys()) >= 1:
        print ('\nListe des contacts favoris :')
        for name, num in repertoire.items():
            print (f'{name} : {num}')
    else:
        return print('\nAucun contact ajouté en favori.'),options()
        
    return options()

def supprimer_fav():
    rep_fav = open("MD_repertoire_fav", "rb")
    repertoire_fav = load(rep_fav)
    rep_fav.close()
    print('')
    contact_recherche = input('Donnez le nom ou le prénom du contact à supprimer de vos favoris : ')
    
    for name in repertoire_fav.keys():
        if contact_recherche.lower()==name[0].lower():
            if name in repertoire_fav.keys():
                del repertoire_fav[name]
                rep_fav = open("MD_repertoire_fav", "wb")
                dump(repertoire_fav,rep_fav)
                rep_fav.close()
                return print(f'\nLe contact {name} à été retiré des favoris !'),options()
        elif contact_recherche.lower()==name[1].lower():
            if name in repertoire_fav.keys():
                del repertoire_fav[name]
                rep_fav = open("MD_repertoire_fav", "wb")
                dump(repertoire_fav,rep_fav)
                rep_fav.close()
                return print(f'\nLe contact {name} à été retiré des favoris !'),options()
            
    return print("\nLe contact est inexistant ou n'est pas dans les favoris"),options()

def supprimer():
    print ('\nATTENTION, cette action est irréversible !')
    avertissement = input ('\nTappez "oui" pour confirmer ou "non" pour annuler : ')
    while avertissement != 'oui' and avertissement != 'non':
        avertissement = input ('\nRéponse invalide. Veuillez taper "oui" pour confirmer ou "non" pour annuler : ')
    if avertissement == 'non':
        return print ('\nAction annulée'),options()
    elif avertissement=='oui':
        rep = open ('MD_repertoire', 'rb')
        repertoire = load (rep)
        rep.close()
    
        contact = input ('\nDonnez le nom ou le prénom du contact à supprimer : ')
        for name in repertoire.keys():
            if contact.lower() == name[0].lower():
                if name in repertoire.keys():
                    del repertoire[name]
                    rep = open ('MD_repertoire', 'wb')
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
    rep = open ('MD_repertoire', 'rb')
    repertoire = load (rep)
    rep.close()
    rep_fav = open ('MD_repertoire_fav', 'rb')
    repertoire_fav = load (rep_fav)
    rep_fav.close()
    
    print ('')
    contact = input ('Donnez le nom ou le prénom du contact à modifier : ')
    nouveau_num = input (f'Entrez un nouveau numéro de téléphone pour {contact} : ')
    for name in repertoire.keys():
        if contact.lower() == name[0].lower():
            if name in repertoire.keys():
                for name_fav in repertoire_fav.keys():
                    if contact.lower() == name[0].lower():
                        if name in repertoire_fav.keys():
                              repertoire_fav[name] = nouveau_num
                              rep_fav = open ('MD_repertoire_fav', 'wb')
                              dump (repertoire_fav, rep_fav)
                              rep_fav.close()
                repertoire[name] = nouveau_num
                rep = open ('MD_repertoire', 'wb')
                dump (repertoire,rep)
                rep.close()
                return print ('\nLe numéro du contact a été modifié !'),options()
        elif contact.lower() == name[1].lower():
            if name in repertoire.keys():
                for name_fav in repertoire_fav.keys():
                    if contact.lower() == name[0].lower():
                        if name in repertoire_fav.keys():
                              repertoire_fav[name] = nouveau_num
                              rep_fav = open ('MD_repertoire_fav', 'wb')
                              dump (repertoire_fav,rep_fav)
                              rep_fav.close()
                repertoire[name] = nouveau_num
                rep = open('MD_repertoire', 'wb')
                dump (repertoire,rep)
                rep.close()
                return print ('\nLe numéro du contact a été modifié !'),options()
                     
    return print ('\nContact inexistant'),options()
      
def la_fin():
    repertoire = {}
    contact1 = ('MESNAGE', 'Dylan')
    num1 = '0665218476'
    contact2 = ('GORLAS', 'Maxime')
    num2 = '0756245841'
    repertoire[contact1] = num1
    repertoire[contact2] = num2
    rep = open ('MD_repertoire','wb')
    dump (repertoire, rep)
    rep.close()
    rep_fav = open ('MD_repertoire_fav','wb')
    dump (repertoire, rep_fav)
    rep_fav.close()
    
    print ('\nLes Crédits :')
    print ('')
    print ('\nLes Créateurs')
    print ('\nGORLAS Maxime')
    print ('MESNAGE Dylan')
    print ('')
    print ('\nLes Cerveaux')
    print ('\nLEMERCIER Guénaël')
    print ('Mr MOUCHEL')
    print ('')
    print ('\nRemerciement Spécial :')
    print ('\nMr MOUCHEL')
    print ('\nMerci d\'avoir essayé notre programme, maintenant, tous les repertoires ont été effacé !')
    return ''
     
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
    print('7-Options SUPER MEGA Spéciales ULTRA 3000')
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
    elif choice=='7':
        return options_super_mega_speciales_ultra_3000()
    else:
        print ('\nChoix impossible\n')
        return options()

def options_super_mega_speciales_ultra_3000():
    print ('\nATTENTION, cette action est irréversible !!!')
    avert = input ('\nTapez "oui" pour confirmer ou "non" pour annuler : ')
    if avert == 'oui':
        avert2 = input ('\nEtes-vous sûr de continuer ??? : ')
        if avert2 == 'oui':
            avert3 = input ("\nDernière chance, si tu es sûr, tape 'je confirme sur l'honneur que je suis sûr de vouloir continuer' : ")
            if avert3 == "je confirme sur l'honneur que je suis sûr de vouloir continuer":
                avert4 = input ("\nToute dernière chance, tout peut s'arrêter ici, là maintenant, tu en as bien conscience ? (Si tu veux continuer, tape 'oui' : ")
                if avert4 == 'oui':
                    print ('\nAu revoir...')
                    return la_fin()
                elif avert4 == 'non':
                    print ('\nBalourd...')
                    return choix()
                else:
                    print ('\nAction Impossible')
                    return options_super_mega_speciales_ultra_3000()
            elif avert3 == 'non':
                print('\nPourquoi faire tout cela pour annuler ???')
                return choix()
            else:
                print ('\nTu écris trop vite je crois... courage !')
                return options_super_mega_speciales_ultra_3000()
        elif avert2 == 'non':
            print ('\nAction annulée, dommage...')
            return choix()
        else:
            print ('\nAction Impossible')
            return options_super_mega_speciales_ultra_3000()
    elif avert == 'non':
        print ('\nAction annulée')
        return choix()
    else:
        print ('\nAction impossible')
        return options_super_mega_speciales_ultra_3000()

choix()

# variable = input ('Pressez "espace"')
# if variable.issplace():
# 	pass