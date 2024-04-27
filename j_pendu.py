from lecture_ecriture import *
from pickle import *
import random
import logging
import os

choice2 = "NONE"
mot = "NONE"

prenoms_liste = ["Dylan", "Flavie", "Gabin", "Luka", "Gladys", "Ellen", "Nathan", "Guenael", "Antoine", "Maxime", "Emelyne", "Loriane", "Enzo", "Matheo", "Colline", "Romain", "Romane", "Ismelie", "Thelma", "Victor", "Nathalie"]
NSI_liste = ["python", "capitalize", "print", "thonny", "for i in range", "while", "repertoire", "pass", "if", "return", "list", "tuple", "set", "dict", "function", "module", "class", "inheritance", "exception", "method", "import", "attribute", "iteration", "recursion", "algorithm", "binary", "search", "sort", "stack", "queue"]
mots_liste = ["boite", "chaussure", "papier", "serviette", "poeme", "ordinateur", "barbie", "cartable", "stylo", "crayon", "livre", "journal", "telephone", "ciseaux", "brochure", "horloge", "cle", "lampe", "calculatrice", "agenda", "stapler", "gobelet", "enveloppe", "ecouteurs"]
instruments_liste = ["piano", "guitare", "saxophone", "triangle", "violon", "vibraphone", "harpe", "contrebasse", "batterie", "flute", "contrebasse", "trompette", "accordeon", "clarinette", "hautbois", "tuba", "xylophone", "cornemuse", "mandoline", "bongo", "tambourin", "sitar", "banjo", "tambour", "clavecin", "orgue", "timbales", "cithare", "didgeridoo", "ukulele"]

def j_pendu():
    global choice2
    logging.info("LANCEMENT JEU: Le Pendu\n")
    
    print ("-- Le Pendu --\n")
    
    print ("1. Les + Beaux Prénoms")
    print ("2. Le Vocabulaire en NSI")
    print ("3. Les Mots et Objets de tous les jours")
    print ("4. Les Instruments de Musique")
    print ("5. Les Contacts de ton Répertoire")
    print ("6. Retour aux choix des jeux\n")
    
    choice2 = input ("Choix : ")
    
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
        os.system ("cls")
        return ""

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
    dico = lecture_csv ("data_contacts.csv")
    
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
        print (f"Mot : {affichage}\n")
        
        choice = input ("Saisir une lettre : ")
        
        if len (choice) == 1 and choice.isalpha() == True:
            
            if choice in lettres_trouvees:
                os.system ("cls")
                print ("Tu as déjà trouvé cette lettre, essayes encore !\n")
            
            elif choice.upper() in mot.upper():
                os.system ("cls")
                print (f"Bien joué, tu as trouvé la lettre \"{choice}\" !\n")
                lettres_trouvees.append(choice)
            
            else:
                tentatives_max -= 1
                tentatives += 1
                os.system ("cls")
                print (f"Cette lettre n\'est pas dans le mot... Plus que {tentatives_max} tentatives !\n")
        
        else:
            os.system ("cls")
            print ("Tu n'as pas tappé une lettre, essaies encore !")
        
        if set(mot.lower()) == set(lettres_trouvees):
            
            if choice2 == "1" or choice2 == "5":
                os.system ("cls")
                print (f"Félicitations, tu as trouvé le prénom \"{mot}\" en seulement {tentatives_max} tentatives ({tentatives} tentatives échouées !\n")
            elif choice2 == '2' or choice2 == '3' or choice2 == '4':
                os.system ("cls")
                print (f"Félicitations, tu as trouvé le mot \"{mot}\" en seulement {tentatives_max} tentatives ({tentatives} tentatives échouées !\n")
            
            return ""
        
        if tentatives_max == 0:
            if choice2 == "1" or choice2 == "5":
                os.system ("cls")
                print (f'Dommage... Tu n\'as pas trouvé le prénom "{mot}"...\n')
            
            elif choice2 == '2':
                print (f'Dommage... Tu n\'as pas trouvé le mot "{mot}"... (t\'es même pas un vrai nerd bouuuu)\n')
            
            elif choice2 == '3':
                os.system ("cls")
                print (f'\nDommage... Tu n\'as pas trouvé le mot "{mot}"...\n')
            
            elif choice2 == '4':
                os.system ("cls")
                print (f'\nDommage... Tu n\'as pas trouvé l\'instrument choisi ({mot})...\n')
            
            return ""