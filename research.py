from pickle import *

def research_f():
    
    rep = open ("repertoire", 'rb')
    dico = load (rep)
    rep.close()
    
    contact = input ('\nDonnez le nom ou le prénom du contact : ')
    
    for name, details in dico.items():
        
        if contact.lower() == name[0].lower() or contact.lower() == name[1].lower():
            
            print (f"\n{name[0]} {name[1]} : {details['num']}\n")
            from choice import choice_f
            return choice_f()
    
    print ('\nAucun contact trouvé !\n')
    from choice import choice_f
    return choice_f()