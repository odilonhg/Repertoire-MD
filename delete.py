from pickle import *

def delete_f():
    
    print ('\nATTENTION, cette action est irréversible !')
    avert = input ('\nTapez "oui" pour confirmer ou "non" pour annuler : ')
    
    while avert != 'oui' and avert != 'non':
        avert = input ('\nRéponse invalide. Veuillez taper "oui" pour confirmer ou "non" pour annuler : ')
        
    if avert == 'non':
        
        print ('\nAction annulée')
        from options import options_f
        return options_f()
    
    elif avert == 'oui':
        
        rep = open ('repertoire', 'rb')
        dico = load (rep)
        rep.close()
    
        contact = input ('\nDonnez le nom ou le prénom du contact à supprimer : ')
        
        for name in dico.keys():
            
            if contact.lower() == name[0].lower():
                
                del dico[name]
                rep = open ('repertoire', 'wb')
                dump (dico,rep)
                rep.close()
                print (f'\nLe contact {name[0]} {name[1]} a été supprimé !')
                from options import options_f
                return options_f()
            
            elif contact.lower() == name[1].lower():
                
                del dico[name]
                rep = open ('repertoire', 'wb')
                dump (dico,rep)
                rep.close()
                print (f'\nLe contact {name[0]} {name[1]} a été supprimé !')
                from options import options_f
                return options_f()
            
        print ("\nLe contact est inexistant !")
        from options import options_f
        return options_f()