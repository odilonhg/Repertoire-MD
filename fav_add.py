from pickle import *

def fav_add_f():
    
    rep = open ("repertoire", 'rb')
    dico = load (rep)
    rep.close()
    
    contact = input ('\nDonnez le nom ou le prénom du contact à ajouter aux favoris : ')
    
    for name in dico.keys():
        
        if contact.lower() == name[0].lower():
            
            if dico[name]['favori'] == True:
                
                print ('\nContact déjà en favori\n')
                from favorites import favorites_f
                return favorites_f()
            
            else:
                
                dico[name]['favori'] = True
                rep = open ("repertoire", 'wb')
                dump (dico, rep)
                rep.close()
                print (f'\nLe contact {name[0]} {name[1]} a été ajouté aux favoris !')
                from favorites import favorites_f
                return favorites_f()
            
        elif contact.lower() == name[1].lower():
            
            if dico[name]['favori'] == True:
                
                print ('\nContact déjà en favori\n')
                from favorites import favorites_f
                return favorites_f()
            
            else:
                
                dico[name]['favori'] = True
                rep = open ("repertoire", 'wb')
                dump (dico, rep)
                rep.close()
                print (f'\nLe contact {name[0]} {name[1]} a été ajouté aux favoris !')
                from favorites import favorites_f
                return favorites_f()
    
    print ('\nContact inexistant !')
    from favorites import favorites_f
    return favorites_f()