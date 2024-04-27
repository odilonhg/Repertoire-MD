from lecture_ecriture import lecture
from lecture_ecriture import joyau
from pickle import *
import random
import logging

choice2 = "NONE"
mot = "NONE"

prenoms_liste = ["Dylan", "Flavie", "Gabin", "Luka", "Gladys", "Ellen", "Nathan", "Guenael", "Antoine", "Maxime", "Emelyne", "Loriane", "Enzo", "Matheo", "Colline", "Romain", "Romane", "Ismelie", "Thelma", "Victor", "Nathalie"]
NSI_liste = ["python", "capitalize", "print", "thonny", "for i in range", "while", "repertoire", "pass", "if", "return", "list", "tuple", "set", "dict", "function", "module", "class", "inheritance", "exception", "method", "import", "attribute", "iteration", "recursion", "algorithm", "binary", "search", "sort", "stack", "queue"]
mots_liste = ["boite", "chaussure", "papier", "serviette", "poeme", "ordinateur", "barbie", "cartable", "stylo", "crayon", "livre", "journal", "telephone", "ciseaux", "brochure", "horloge", "cle", "lampe", "calculatrice", "agenda", "stapler", "gobelet", "enveloppe", "ecouteurs"]
instruments_liste = ["piano", "guitare", "saxophone", "triangle", "violon", "vibraphone", "harpe", "contrebasse", "batterie", "flute", "contrebasse", "trompette", "accordeon", "clarinette", "hautbois", "tuba", "xylophone", "cornemuse", "mandoline", "bongo", "tambourin", "sitar", "banjo", "tambour", "clavecin", "orgue", "timbales", "cithare", "didgeridoo", "ukulele"]

def j_pendu():
    global choice2
    logging.info("LANCEMENT JEU: Le Pendu\n")
    
    print ("\nOh, un joueur !")
    print ("Je me présente, je suis JoyEAU, gardien du joyau de la puissance.")
    print ("Tu le veux ? Et bien gagnes au Pendu !")
    
    print ("\n--- Le Pendu ---\n")
    
    print ("1. Les + Beaux Prénoms")
    print ("2. Le Vocabulaire en NSI")
    print ("3. Les Mots et Objets de tous les jours")
    print ("4. Les Instruments de Musique")
    print ("5. Les Contacts de ton Répertoire")
    print ("6. Retour aux choix des jeux")
    
    choice2 = input ("\nChoix : ")
    
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
    
    affichage = ""
    
    for lettre in mot:
        if lettre.lower() in lettres_trouvees:
            affichage += lettre
        else:
            affichage += "_"
    
    return affichage

def le_pendu_lancement():
    prenoms_contacts_liste = []
    dico = lecture("Repertoire MD.csv")
    
    for contacts in dico:
        
        prenom = contacts["prenom"]
        prenoms_contacts_liste.append(prenom)
    
    global choice2, mot, prenoms_liste, NSI_liste, mots_liste, instruments_liste, joyau
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
        print (f"\nMot : {affichage}\n")
        
        choice = input ("Saisir une lettre : ")
        
        if len (choice) == 1 and choice.isalpha() == True:
            
            if choice in lettres_trouvees:
                print ("\nTu as déjà trouvé cette lettre, essayes encore !")
            
            elif choice.upper() in mot.upper():
                print (f"\nBien joué, tu as trouvé la lettre \"{choice}\" !")
                lettres_trouvees.append(choice)
            
            else:
                tentatives_max -= 1
                tentatives += 1
                print (f"\nCette lettre n\'est pas dans le mot... Plus que {tentatives_max} tentatives !")
        
        else:
            print ("\nTu n'as pas tappé une lettre, essaies encore !")
        
        if set(mot.lower()) == set(lettres_trouvees):
            
            if choice2 == "1" or choice2 == "5":
                print (f"\nFélicitations, tu as trouvé le prénom \"{mot}\" en seulement {tentatives_max} tentatives ({tentatives} tentatives échouées !\nVoilà mon joyau...")
            elif choice2 == '2' or choice2 == '3' or choice2 == '4':
                print (f"\nFélicitations, tu as trouvé le mot \"{mot}\" en seulement {tentatives_max} tentatives ({tentatives} tentatives échouées !\nVoilà mon joyau...")
            
            joyau +=1
            
            from j_choix import j_choix
            return j_choix()
        
        if tentatives_max == 0:
            if choice2 == "1" or choice2 == "5":
                print (f'\nDommage... Tu n\'as pas trouvé le prénom "{mot}"...')
            
            elif choice2 == '2':
                print (f'\nDommage... Tu n\'as pas trouvé le mot "{mot}"... (t\'es même pas un vrai nerd bouuuu)')
            
            elif choice2 == '3':
                print (f'\nDommage... Tu n\'as pas trouvé le mot "{mot}"...')
            
            elif choice2 == '4':
                print (f'\nDommage... Tu n\'as pas trouvé l\'instrument choisi ({mot})...')
            
            from j_choix import j_choix
            return j_choix()