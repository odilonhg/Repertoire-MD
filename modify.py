from pickle import *

def modify_f():
    
    rep = open ('repertoire', 'rb')
    dico = load (rep)
    rep.close()
    
    print ('\nQue souhaitez-vous modifier ?')
    print ('1. Le nom')
    print ('2. Le prénom')
    print ('3. Le numéro de téléphone\n')
    
    choice = input ('Choix : ')
    
    def modify_prenom():
        
        contact = input ('\nDonnez le nom ou le prénom du contact : ')
        
        for name, details in dico.items():
            
            if contact.lower() == name[0].lower() or contact.lower() == name[1].lower():
                    
                prenom = input (f'\nSaisir le nouveau prénom de {name[0]} {name[1]} : ').capitalize()
                nom = name[0]
                num = details['num']
                favori = details['favori']
                cle = (nom, prenom)
                
                del dico[name]
                dico[cle] = {'num': num, 'favori': favori}
                
                rep = open ('repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {name[0]} {name[1]} a été modifié !')
                
                from options import options_f
                return options_f()
        
        print ('\nContact inexistant')
        from options import options_f
        return options_f()
        
    def modify_nom():
        
        contact = input ('\nDonnez le nom ou le prénom du contact : ')
        
        for name, details in dico.items():
            
            if contact.lower() == name[0].lower() or contact.lower() == name[1].lower():
                
                nom = input (f'\nSaisir le nouveau nom de {name[0]} {name[1]} : ').upper()
                prenom = name[1]
                num = details['num']
                favori = details['favori']
                cle = (nom, prenom)
                
                del dico[name]
                dico[cle] = {'num': num, 'favori': favori}
                
                rep = open ('repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {name[0]} {name[1]} a été modifié !')
                
                from options import options_f
                return options_f()
        
        print ('\nContact inexistant')
        from options import options_f
        return options_f()
        
    def modify_num():
        
        contact = input ('\nDonnez le nom ou le prénom du contact : ')
        
        for name, details in dico.items():
            
            if contact.lower() == name[0].lower() or contact.lower() == name[1].lower():
                
                num = input (f'\nSaisir le nouveau numéro de téléphone de {name[0]} {name[1]} : ')
                
                details['num'] = num
                
                rep = open ('repertoire', 'wb')
                dump (dico, rep)
                rep.close()
                
                print (f'\nLe contact {name[0]} {name[1]} a été modifié !')
                
                from options import options_f
                return options_f()
        
        print ('\nContact inexistant')
        from options import options_f
        return options_f()
    
    if choice == '1':
        return modify_nom()
    
    elif choice == '2':
        return modify_prenom()
    
    elif choice == '3':
        return modify_num()
    
    else:
        print ('\nChoix Impossible !')
        from options import options_f
        return options_f()