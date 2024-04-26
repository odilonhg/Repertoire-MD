def opt_special_f():
    
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
                    from the_end import the_end_f
                    return the_end_f()
                
                elif avert4 == 'non':
                    print ('\nBalourd...')
                    from options import options_f
                    return options_f()
                
                else:
                    print ('\nAction Impossible')
                    return opt_special_f()
                
            elif avert3 == 'non':
                print('\nPourquoi faire tout cela pour annuler ???')
                from options import options_f
                return options_f()
            
            else:
                print ('\nTu écris trop vite je crois... courage !')
                return opt_special_f()
            
        elif avert2 == 'non':
            print ('\nAction annulée, dommage...')
            from options import options_f
            return options_f()
        
        else:
            print ('\nAction Impossible')
            return opt_special_f()
        
    elif avert == 'non':
        print ('\nAction annulée')
        from options import options_f
        return options_f()
    
    else:
        print ('\nAction impossible')
        return opt_special_f()