# NOUVEAU STANDARD (+ SIMPLE):

dico = {}
dico[0] = {}

dico [0]['nom'] = 'MESNAGE'
dico [0]['prenom'] = 'Dylan'

print ( f'dico = {dico}' )
print ( dico[0]['prenom'].upper() )
print()

# POUR INDIQUER DANS UNE FONCTION QU'YNE VARIABLE EST "GLOBALE" (contenue en dehors de la fonction):

global variable

# EXEMPLE CONTACT COMPLET:

mois_nombre = {
    1: '01',
    2: '02',
    3: '03',
    4: '04',
    5: '05',
    6: '06',
    7: '07',
    8: '08',
    9: '09',
    10: '10',
    11: '11',
    12: '12'
    }

mois_lettre = {
    1: 'Janvier',
    2: 'Février',
    3: 'Mars',
    4: 'Avril',
    5: 'Mai',
    6: 'Juin',
    7: 'Juillet',
    8: 'Août',
    9: 'Septembre',
    10: 'Octobre',
    11: 'Novembre',
    12: 'Décembre'
    }

mois = mois_nombre[mois_c]
mois2 = mois_lettre[mois_c]

dico[len(dico.keys())] = {}
dico[max(dico.keys())]['nom'] = nom
dico[max(dico.keys())]['prenom'] = prenom
dico[max(dico.keys())]['jour'] = jour
dico[max(dico.keys())]['mois'] = mois
dico[max(dico.keys())]['mois2'] = mois2
dico[max(dico.keys())]['annee'] = annee
dico[max(dico.keys())]['num'] = num
dico[max(dico.keys())]['email'] = email
dico[max(dico.keys())]['favori'] = favori

# DIFFERENTS FICHIERS:

fichier_log = 'log.txt'
fichier_repertoire = 'MD_repertoire'

# UTILISATION DE 'PICKLE'

from pickle import *

rep = open (fichier_repertoire, 'rb')
dico = load (rep)
rep.close()

rep = open (fichier_repertoire, 'wb')
dump (dico, rep)
rep.close()

# UTILISATION DE 'OS' (en lien avec les différents fichiers):

import os

if os.path.exists(fichier_log) == True:
    print ('le fichier existe !')

else:
    print ('le fichier n\'existe pas !')

print()

# UTILISATION DE 'logging' (fichier log.txt):

import logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('VOTRE LOG ICI\n')

# NOUVELLE FICHIER: depart.py
# Ce fichier se lance losque le répertoire est démarré pour la 1ère fois !

# EXEMPLE UTILISATION FONCTION max():

b = 'b'
d = 'd'

dico = {}
dico [0] = {}
dico [max(dico.keys())]['a'] = b
dico [max(dico.keys())]['c'] = d

