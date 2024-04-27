import csv
import pickle

def lecture_csv(rep, delimiter = ";"):
    liste=[]
    
    try:
        with open (rep, "r") as csvfile:
            cles=csvfile.readline().strip().split(delimiter)
            
            for ligne in csvfile:
                datas=ligne.strip().split(delimiter)
                liste.append(dict(zip(cles,datas)))
            
    except:
        return []
    
    return liste

def ecriture_csv(rep, liste, delimiter = ";"):
    
    with open (rep, "w") as csvfile:
        ligneDesc = ";".join(liste[0].keys()) + "\n"
        csvfile.write (ligneDesc)
        
        for cle in range(len(liste)):
            ligne = ";".join(liste[cle].values()) + "\n"
            csvfile.write (ligne)

def lecture_pickle (fichier):
    try:
        with open (fichier, "rb") as f:
            liste = pickle.load (f)
        return liste
    except:
        return []
def ecriture_pickle (donnees, fichier):
    with open (fichier, "wb") as f:
        pickle.dump (donnees, f)