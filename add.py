from pickle import *

def add_f():
    
    rep = open ('repertoire', 'rb')
    dico = load (rep)
    rep.close()
    
    nom = input ('\nSaisir le nom du contact : ').upper()
    prenom = input ('Saisir le prénom du contact : ').capitalize()
    
    if nom == '' or prenom == '':
        print ('\nChoix du nom et/ou du prénom impossible !\n')
        from choice import choice_f
        return choice_f()
    
    cle = (nom, prenom)
    num = input ('Saisir le numéro de téléphone du contact : ')
    favori = False
    dico[cle] = {'num': num, 'favori': favori}
    
    rep = open ('repertoire', 'wb')
    dump (dico, rep)
    rep.close()
    
    print('')
    print (f'Le contact {cle[0]} {cle[1]} a été ajouté !')
    print('')
    
    from choice import choice_f
    return choice_f()