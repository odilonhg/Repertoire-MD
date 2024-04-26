from pickle import *

def display_f():
    
    rep = open ("repertoire", 'rb')
    dico = load (rep)
    rep.close()
    
    if len (dico.keys()) >= 1:
        print ('\n--- Liste des contacts ---\n')
        for name, details in dico.items():
            print (f"{name[0]} {name[1]} : {details['num']}")
        print('')
    else:
        print ('\nAucun contact trouvé.\n')
        from choice import choice_f
        return choice_f()
        
    from choice import choice_f
    return choice_f()