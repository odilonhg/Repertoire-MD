from pickle import *
import random
import logging

choice2 = 'NONE'
mot = "NONE"

rep = open ('MD_repertoire', 'rb')
dico = load (rep)
rep.close()

prenoms_liste = ['Dylan','Flavie','Gabin','Luka','Gladys','Ellen','Nathan','Guenael','Antoine','Maxime','Emelyne','Loriane','Enzo','Matheo','Colline']
NSI_liste = ['python','capitalize','print','thonny','for i in range','while','repertoire','pass','if','return']
mots_liste = ['boite','chaussure','papier','serviette','poeme','ordinateur','barbie','cartable']
instruments_liste = ['piano','guitare','saxophone','triangle','violon','vibraphone','harpe','contrebasse','batterie','flute','contrebasse','trompette','accordeon','clarinette']
prenoms_contacts_liste = []

for indice, contacts in dico.items():
    
    prenom = contacts.get ('prenom')
    prenoms_contacts_liste.append (prenom)

def le_pendu():
    
    global choice2
    logging.info('LANCEMENT DE JEU: Le Pendu\n')
    
    print ('\nBienvenue dans le Pendu !')
    
    choice = input ('\nAvez-vous déjà joué ? ').upper()
    
    if choice == 'NON':
        print ('\nLe jeu du Pendu, c\'est simple, tu vas choisir un thème et tu devras ensuite trouver le mot que je caches en lien avec ce thème !')
        print ('C\'est parti !')
    
    print ('\n--- Le Pendu ---\n')
    
    print ('1. Les Prénoms (de mes amis)')
    print ('2. Le Vocabulaire en NSI')
    print ('3. Les Mots (de la vie de tous les jours)')
    print ('4. Les Instruments de musique')
    print ('5. Les Contacts (en création...)')
    print ('6. Retour aux choix des jeux')
    
    choice2 = input ('\nChoix : ')
    
    if choice2 == '1':
        return le_pendu_lancement()
    
    elif choice2 == '2':
        return le_pendu_lancement()
    
    elif choice2 == '3':
        return le_pendu_lancement()
    
    elif choice2 == '4':
        return le_pendu_lancement()
    
    elif choice2 == '5':
        return le_pendu_lancement()
    
    elif choice2 == '6':
        from c_options.jeux.choix_j import choix_j
        return choix_j()

def affichage_mot(mot, lettres_trouvees):
    
    affichage = ''
    
    for lettre in mot:
        if lettre.lower() in lettres_trouvees:
            affichage += lettre
        else:
            affichage += '_'
    
    return affichage

def le_pendu_lancement():
    
    global choice2, mot, prenoms_liste, NSI_liste, mots_liste, instruments_liste, prenoms_contacts_liste
    lettres_trouvees = []
    tentatives_max = 6
    tentatives = 0
    
    if choice2 == '1':
        mot = random.choice (prenoms_liste)
    
    elif choice2 == '2':
        mot = random.choice (NSI_liste)
    
    elif choice2 == '3':
        mot = random.choice (mots_liste)
    
    elif choice2 == '4':
        mot = random.choice (instruments_liste)
    
    elif choice2 == '5':
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
            
            if choice2 == '1' or choice2 == '5':
                print (f'\nFélicitations, tu as trouvé le prénom "{mot}" en seulement {tentatives} tentatives échouées !')
            elif choice2 == '2' or choice2 == '3' or choice2 == '4':
                print (f'\nFélicitations, tu as trouvé le mot "{mot}" en seulement {tentatives} tentatives échouées !')
                 
            from c_options.jeux.choix_j import choix_j
            return choix_j()
        
        if tentatives_max == 0:
            if choice2 == '1' or choice2 == '5':
                print (f'\nDommage... Tu n\'as pas trouvé le prénom "{mot}"...')
            
            elif choice2 == '2':
                print (f'\nDommage... Tu n\'as pas trouvé le mot "{mot}"... (t\'es même pas un vrai nerd bouuuu)')
            
            elif choice2 == '3':
                print (f'\nDommage... Tu n\'as pas trouvé le mot "{mot}"...')
            
            elif choice2 == '4':
                print (f'\nDommage... Tu n\'as pas trouvé l\'instrument choisi ({mot})...')
            
            from c_options.jeux.choix_j import choix_j
            return choix_j()