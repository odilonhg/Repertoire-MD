from pickle import *

def ajoute():
    rep=open('MD_repertoire','rb')
    repertoire=load(rep)
#     print(repertoire)
    rep.close()
    
    nom=input('\nSaisir le nom du contact : ').upper()
    prenom=input('Saisir le prénom du contact : ').capitalize()
    cle=(nom,prenom)
#     print(cle)
    num=input('Saisir le numéro de téléphone du contact : ')
    repertoire[cle]=num
#     print(repertoire)
    
    rep=open('MD_repertoire','wb')
    dump(repertoire,rep)
    rep.close()
    return choix()

def recherche():
    rep=open("MD_repertoire",'rb')
    dico_recherche=load(rep)
    rep.close()
#     print(dico_recherche)
    contact_recherche=input('\nDonnez le nom ou le prénom du contact : ')
    for name in dico_recherche.keys():
#         print(name)
        if contact_recherche.lower() == name[0].lower():
            print(name, ':', dico_recherche[name])
        if contact_recherche.lower() == name[1].lower():
            print(name, ':', dico_recherche[name])
    return choix()

def affiche():
    rep=open("MD_repertoire",'rb')
    repertoire=load(rep)
    rep.close()
    print(repertoire)
    return choix()

def choix():
    print('1-Rechercher un contact')
    print('2-Ajouter un contact')
    print('3-Afficher les contacts')
    print('4-Quitter')
    choice=input("Choix : ")
    if choice=="4":
        return ""
    elif choice=="1":
        return recherche()
    elif choice=="2":
        return ajoute()
    elif choice=="3":
        return affiche()
    else:
        print('\nChoix impossible\n')
        return choix()

choix()

# z=open("MD_repertoire",'wb')
