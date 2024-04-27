import pickle
import random
import datetime
import shutil
import os

from lecture_ecriture import *

f_taches = "data_gdt"
l_taches = []

def load (fichier):
    try:
        with open (fichier, "rb") as f:
            liste = pickle.load (f)
        return liste
    except:
        return []
def save (donnees, fichier):
    with open (fichier, "wb") as f:
        pickle.dump (donnees, f)

def time_task (date):
    date_debut = datetime.datetime.now()
    date_fin = date
    date_fin = datetime.datetime.combine(date_fin, datetime.time.min)
    temps_restant = date_fin - date_debut
    jours_restants = temps_restant.days
    heures_restantes = temps_restant.seconds // 3600
    minutes_restantes = (temps_restant.seconds % 3600) // 60
    temps_restant = str(jours_restants) + ":" + str(heures_restantes) + ":" + str(minutes_restantes)
    return temps_restant

def show_tasks (l_taches):
    print ("--- Liste des Tâches ---")
    print ("* = tâche terminée")
    
    for i, tache in enumerate (l_taches, start = 1):
        date = tache["date_maxi"]
        tps_restant = time_task (date)
        if tache["etat"] == True:
            print (f'\n{i}.   | {tache["description"]}')
            print (f'     | Date d\'échéance : {date}')
            print (f'     | Temps restant : {tps_restant}')
        else:
            print (f'\n{i}. * | {tache["description"]}')
            print (f'     | Date d\'échéance : {tache["date_maxi"]}')
            print (f'     | Temps restant : {tps_restant}')

def add_task (description, date_maxi, l_taches):
    nouvelle_tache = {"description": description, "date_maxi": date_maxi, "etat": True}
    l_taches.append (nouvelle_tache)
    print ("\nTâche ajoutée avec succès !\n")

def end_task (description, liste_taches):
    for tache in liste_taches:
        desc = tache["description"]
        if description.lower () == desc.lower ():
            print (f'\nMettre fin à la tâche "{desc}" ?')
            choix = input ('Saisir "oui" ou "non" : ').lower ()
            
            if choix == "oui":
                tache["etat"] = False
                print ("\nTâche marquée comme terminée !\n")
                return ""
            else:
                print ()
                return ""
    print ("\nAucune tâche ne porte ce nom.\n")

def clean_tasks (l_taches):
    new_liste = []
    for i in range (len (l_taches)):
        if l_taches[i]["etat"] == True:
            new_liste.append (l_taches[i])
    save (new_liste, f_taches)

def gdt_choix ():
    global l_taches
    l_taches = lecture_pickle (f_taches)
    
    print ("--- Gestionnaire de Tâches MD ---\n")
    print ("1. Afficher les tâches")
    print ("2. Ajouter une tâche")
    print ("3. Finir une tâche")
    print ("4. Effacer les tâches accomplies")
    print ("5. Retour au Repertoire MD\n")
    
    choix = input ("Choix : ")
    
    match choix:
        
        case "1":
            os.system ("cls")
            show_tasks (l_taches)
            print ()
            return gdt_choix ()
        case "2":
            os.system ("cls")
            print ("--- Ajouter une Tâche ---")
            description = input ("\nNom de la tâche : ")
            date_maxi_str = input ("\nEntrer la date d'échéance (AAAA-MM-JJ) : ")
            date_maxi = datetime.datetime.strptime (date_maxi_str, "%Y-%m-%d").date ()
            add_task (description, date_maxi, l_taches)
            ecriture_pickle (l_taches, f_taches)
            return gdt_choix ()
        case "3":
            os.system ("cls")
            show_tasks (l_taches)
            description = input ("\nSaisir le nom de la tâche terminée : ")
            end_task (description, l_taches)
            ecriture_pickle (l_taches, f_taches)
            return gdt_choix ()
        case "4":
            clean_tasks (l_taches)
            os.system ("cls")
            return gdt_choix ()
        case "5":
            return ""
        case "13":
            os.system ("cls")
            from choix import choix
            return choix()
        case _:
            os.system ("cls")
            print ("Choix impossible.\n")
            return gdt_choix ()