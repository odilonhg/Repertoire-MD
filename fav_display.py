from pickle import *

def fav_display_f():

    rep = open ("repertoire", 'rb')
    dico = load (rep)
    rep.close()
    
    flag = False
    
    for name, details in dico.items():
        if details['favori'] == 'True':
            flag = True
            
    if flag == True:
        
        print ('\n--- Liste des favoris ---\n')
        for name, details in dico.items():
            if details['favori'] == 'True':
                print (f"{name[0]} {name[1]} : {details['num']}")
                
        from favorites import favorites_f
        return favorites_f()
    
    else:
        print ('\nAucun contact favori trouvé !')
        from favorites import favorites_f
        return favorites_f()