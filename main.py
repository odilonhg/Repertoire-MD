from lecture_ecriture import *
from choix import choix
import datetime
import random
import logging
import os

f_log = "log.txt"
f_rep = "data_contacts.csv"
f_user = "data_user"
f_groupes = "data_groupes.csv"
f_son = "data_son"

if os.path.exists (f_log) == False:
    
    logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    
    os.system ("cls")
    nom_user = input ("Saisir votre prénom : ").capitalize ()
    print ("\nVoulez-vous une ambiance sonore ? (désactivable par la suite)\n")
    choice = input ("Choix : ").upper ()
    if choice == "NON":
        choix3 = False
    else:
        choix3 = True
    ecriture_pickle (choix3, f_son)
    ecriture_pickle (nom_user, f_user)
    logging.info (f"Bienvenue à toi {nom_user} dans le Repertoire MD !\n")
    os.system ("cls")

else:
    
    logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
    logging.info ("OUVERTURE PROGRAMME\n")
    
    nom_user = lecture_pickle (f_user)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages_salutations = [
        f"Bonjour {nom_user}\n! Horloge : {date}.",
        f"Salut {nom_user} !\nHorloge : {date}.",
        f"Holà {nom_user} !\nHorloge : {date}.",
        f"Coucou {nom_user} !\nHorloge : {date}.",
        f"Hello {nom_user} !\nHorloge : {date}.",
        f"Salutations {nom_user} !\nHorloge : {date}.",
        f"Hey {nom_user} !\nHorloge : {date}.",
        f"Wesh {nom_user} !\nT'as trouvé mon message secret, mais le dis à personne !",
        f"Hey hey {nom_user}, savais-tu que MD c'était pour MaximeDylan (les 2 créateurs de la Team) ?\nHorloge : {date}.",
        f"Bien le bonjour {nom_user}, j'espère que tu vas bien !\nHorloge : {date}",
        f"Hé {nom_user}, comment tu vas ?\nHorloge : {date}",
    ]
    num_aleatoire = random.randint(1, 10)
    
    os.system ("cls")
    print (messages_salutations[num_aleatoire])
    print ()

choix2 = lecture_pickle (f_son)

if choix2 == True:
    import pygame
    pygame.init()
    soundtrack = "audio/musique1.mp3"
    pygame.mixer.music.load(soundtrack)
    pygame.mixer.music.play(start = random.randint(1, 3600))

choix ()