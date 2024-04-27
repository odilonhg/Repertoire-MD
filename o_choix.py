import os
import pygame
import subprocess
import random
from lecture_ecriture import *

f_son = "data_son"

fortnite = "C:\Program Files\Epic Games\Fortnite\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping.exe"

def lancer_exe(nom_fichier):
    try:
        chemin_absolu = os.path.abspath(nom_fichier)
        subprocess.run(chemin_absolu, shell=True)
        return True
    except Exception as e:
        return False

def o_choix ():
    choix = lecture_pickle (f_son)
    print ("--- Les Options ---\n")
    
    print ("0. Annuler")
    if choix == True:
        print ("1. Couper la musique")
    else:
        print ("1. Lancer la musique")
    print ("2. Changer la langue")
    print ("3. Lancer un programme de ton ordi")
    print ("4. Disparaître\n")
    
    choice = input ("Choix : ")
    
    match choice:
        
        case "0":
            return ""
        
        case "1":
            if choix == True:
                pygame.init()
                os.system ("cls")
                soundtrack = "audio/musique1.mp3"
                
                pygame.mixer.music.load(soundtrack)
                pygame.mixer.music.stop()
                choix = False
                ecriture_pickle (choix, f_son)
                return ""
            else:
                pygame.init()
                os.system ("cls")
                soundtrack = "audio/musique1.mp3"
                
                pygame.mixer.music.load(soundtrack)
                pygame.mixer.music.play(start = random.randint(1, 3600))
                choix = True
                ecriture_pickle (choix, f_son)
                return ""
        
        case "2":
            os.system ("cls")
            print ("---- MD Center ----\n")
            
            print ("1. Répertoire de Contacts")
            print ("2. Névjegyzék")
            print ("3. Speciális funkcióközpont")
            print ("4. Feladatkezelő")
            print ("5. MDP menedzser")
            print ("6. Lehetőségek")
            print ("7. Állj meg\n")
            
            choice2 = input ("Választás : ")
            
            match choice:
                
                case "13":
                    os.system ("cls")
                    print ("T'es un p'tit génie toi !\n")
                    from choix import choix
                    return choix()
                
                case _:
                    os.system ("cls")
                    print ("Bon la blague est pas drôle...\n")
                    return o_choix ()
        
        case "4":
            lancer_exe("unins000.exe")
            os._exit (0)
        
        case "3":
            if lancer_exe(fortnite) == "True":
                os.system ("cls")
                print ("Jeu lancé: Fortnite\n")
                return o_choix ()
            os.system ("cls")
            print ("Aucun programme affilié n'est installé !\n")
            return o_choix ()
        
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()