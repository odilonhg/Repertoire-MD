from lecture_ecriture import joyau
import sys
import logging

def choix():
    global joyau
    
    print ("--- Répertoire MD ---\n")
    
    print ("1. Gérer les contacts")
    print ("2. Gérer les favoris")
    print ("3. Options")
    print ("4. Arrêter\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "1":
            from c_choix import c_choix
            return c_choix()
        
        case "2":
            from f_choix import f_choix
            return f_choix()
        
        case "3":
            from o_choix import o_choix
            return o_choix()
        
        case "4":
            logging.info("FERMETURE PROGRAMME\n")
            sys.exit("Fermeture du programme")
        
        case "13":
            print ("\nTu m\'as trouvé...")
            print ("Moi, c'est JoyO !\n")
            logging.info("JOYO TROUVE !\n")
            
            match joyau:
                
                case 0:
                    print ("Voici un joyau secret, trouves les 2 autres pour débloquer la fonction spéciale !\n")
                case 1:
                    print ("Voilà mon joyau secret, trouves le dernier pour débloquer la fonction spéciale !\n")
                case 2:
                    print ("Woaw, tu nous as tous trouvé !\n")
                    print ("Voilà mon joyau secret, pour accéder à la fonction spéciale, tapes \"CodeS\" ici !\n")
                
            joyau += 1
            
            return choix()
        
        case "CodeS":
            if joyau == 3:
                print ("\nBien joué !")
                from o_fonction_speciale import o_fonction_speciale
                return o_fonction_speciale()
            else:
                print ("Tu n'as pas trouvé les 3 joyaux sacrés !\nReviens quand tu les auras trouvé !\n")
                return choix()
            
        case _:
            print ("\nChoix impossible...\n")
            return choix()