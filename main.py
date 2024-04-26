import os
import logging
from pickle import *

fichier_log = 'log.txt'
fichier_repertoire = 'MD_repertoire'

if os.path.exists (fichier_log) == False:
    
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info ('Le programme a été ouvert pour la 1ère fois !\n')
    
    from depart import depart
    depart()

else:
    
    logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    logging.info ('OUVERTURE PROGRAMME\n')

from choix import choix
choix()