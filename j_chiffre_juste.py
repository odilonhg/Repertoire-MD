from random import *
import logging
import os

def j_chiffre_juste():
    
    logging.info('LANCEMENT JEU: Le Chiffre Juste\n')
    nombre_a_trouver = randint (0, 100)
    tentatives = 0
    
    mon_nombre = int (input ('Saisir ton nombre : ') )
    
    while mon_nombre != nombre_a_trouver:
        
        if mon_nombre < nombre_a_trouver:
            os.system ("cls")
            print ('Trop petit !')
        
        elif mon_nombre > nombre_a_trouver:
            os.system ("cls")
            print ('Trop grand !')
        
        tentatives +=1
        
        mon_nombre = int (input ('\nSaisir un autre nombre : ') )
    
    os.system ("cls")
    print (f'Bien joué, tu as trouvé mon nombre ({nombre_a_trouver}) en {tentatives} tentatives !\n')
    return ""