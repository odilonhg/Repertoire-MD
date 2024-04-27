from random import *
import logging

def j_chiffre_juste():
    
    logging.info('LANCEMENT JEU: Le Chiffre Juste\n')
    nombre_a_trouver = randint (0, 100)
    tentatives = 0
    
    print ('\nBienvenue dans le Chiffre Juste !\n')
    choice = input ('Avez-vous déjà jouer ? ').upper()
    
    if choice == 'NON':
        
        print ('\nLe jeu est simple, je vais tirer un nombre aléatoire entre 1 et 100')
        print ('Toi, tu vas devoir trouver ce nombre, je vais te dire si il est trop grand, ou trop petit')
        print ('C\'est parti !')
    
    mon_nombre = int (input ('\nSaisir ton nombre : ') )
    
    while mon_nombre != nombre_a_trouver:
        
        if mon_nombre < nombre_a_trouver:
            print ('\nTrop petit !')
        
        elif mon_nombre > nombre_a_trouver:
            print ('\nTrop grand !')
        
        tentatives +=1
        
        mon_nombre = int (input ('\nSaisir un autre nombre : ') )
    
    print (f'\nBien joué, tu as trouvé mon nombre ({nombre_a_trouver}) en {tentatives} tentatives !')
    from j_choix import j_choix
    return j_choix()