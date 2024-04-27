from lecture_ecriture import lecture
import os
import logging
f_log = "log.txt"
f_rep = "Repertoire MD.csv"

if os.path.exists (f_log) == False:
    
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info ('Bienvenue dans le Repertoire MD !\n')
    
    from depart import depart
    depart()

else:
    
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info ('OUVERTURE PROGRAMME\n')

from choix import choix
choix()