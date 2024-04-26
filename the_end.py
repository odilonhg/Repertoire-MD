from pickle import *

import pygame # PENSEZ A INSTALLER LE PLUGIN PYGAME AVEC LA COMMANDE "pip install pygame"
pygame.init()

def the_end_f():
    
    soundtrack = "the_end.mp3"
    
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.play(start = 75)
    
    dico = {}
    favori = 'True'
    
    contact1 = ('MESNAGE', 'Dylan')
    num1 = '0665218476'
    
    contact2 = ('GORLAS', 'Maxime')
    num2 = '0756245841'
    
    dico[contact1] = {'num': num1, 'favori': favori}
    dico[contact2] = {'num': num2, 'favori': favori}
    
    rep = open ('repertoire','wb')
    dump (dico, rep)
    rep.close()
    
    print ('\nLes Crédits :\n')
    
    pygame.time.delay(5000)
    print ('\nLes Créateurs')
    
    pygame.time.delay(3000)
    print ('\nGORLAS Maxime')
    
    pygame.time.delay(3000)
    print ('MESNAGE Dylan\n')
    
    pygame.time.delay(5000)
    print ('\nLes Cerveaux')
    
    pygame.time.delay(3000)
    print ('\nLEMERCIER Guénaël')
    
    pygame.time.delay(3000)
    print ('Mr MOUCHEL\n')
    
    pygame.time.delay(5000)
    print ('\nRemerciements Spéciaux')
    
    pygame.time.delay(3000)
    print ('\nMr MOUCHEL')
    
    pygame.time.delay(3000)
    print ('Toi, qui as essayé notre répertoire !')
    
    pygame.time.delay(5000)
    print ('\nMerci d\'avoir essayé notre programme, le répertoire est à présent réinitialisé !')
    
    pygame.time.delay(5000)
    return ''