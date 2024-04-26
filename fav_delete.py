from pickle import *

def fav_delete_f():
    
    rep = open("repertoire", "rb")
    dico = load(rep)
    rep.close()
    
    contact = input ('\nDonnez le nom ou le prénom du contact à supprimer de vos favoris : ')
    
    for name, details in dico.items():
        
        if contact.lower() == name[0].lower():
            
            if details['favori'] == True:
                
                dico[name]['favori'] = False
                rep = open("repertoire", "wb")
                dump (dico, rep)
                rep.close()
                print(f'\nLe contact {name[0]} {name[1]} à été retiré des favoris !')
                from favorites import favorites_f
                return favorites_f()
            
        elif contact.lower() == name[1].lower():
            
            if details['favori'] == True:
                
                dico[name]['favori'] = False
                rep = open("repertoire", "wb")
                dump (dico, rep)
                rep.close()
                print(f'\nLe contact {name[0]} {name[1]} à été retiré des favoris !')
                from favorites import favorites_f
                return favorites_f()
    
    print ("\nLe contact est inexistant ou n'est pas dans les favoris\n")
    from favorites import favorites_f
    return favorites_f