from pickle import *
import random

mot = "NONE"

rep = open ('MD_repertoire', 'rb')
dico = load (rep)
rep.close()

prenoms_contacts_liste = []

for indice, contacts in dico.items():
    
    prenom = contacts.get ('prenom')
    prenoms_contacts_liste.append (prenom)

def affichage_mot(mot, lettres_trouvees):
    
    affichage = ''
    
    for lettre in mot:
        if lettre.lower() in lettres_trouvees:
            affichage += lettre
        else:
            affichage += '_'
    
    return affichage

def pendu_special():
    
    global mot, prenoms_contacts_liste
    lettres_trouvees = []
    tentatives_max = 6
    tentatives = 0
    
    mot = random.choice (prenoms_contacts_liste)
    
    while tentatives_max >= 0:
        
        affichage = affichage_mot (mot, lettres_trouvees)
        print (f'\nMot : {affichage}\n')
        
        choice = input ('Saisir une lettre : ')
        
        if len (choice) == 1 and choice.isalpha() == True:
            
            if choice in lettres_trouvees:
                print ('\nTu as déjà trouvé cette lettre, essayes encore !')
            
            elif choice.upper() in mot.upper():
                print (f'\nBien joué, tu as trouvé la lettre "{choice}" !')
                lettres_trouvees.append(choice)
            
            else:
                tentatives_max -= 1
                tentatives += 1
                print (f'\nCette lettre n\'est pas dans le mot... Plus que {tentatives_max} tentatives !')
        
        else:
            print ('\nTu n\'as pas tappé une lettre, essaies encore !')
        
        if set(mot.lower()) == set(lettres_trouvees):
            
            return True
        
        if tentatives_max == 0:
            
            return False