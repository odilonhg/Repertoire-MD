import csv
joyau = 0

def lecture(rep, delimiter = ";"):
    liste=[]
    
    with open (rep, "r") as csvfile:
        cles=csvfile.readline().strip().split(delimiter)
        
        for ligne in csvfile:
            datas=ligne.strip().split(delimiter)
            liste.append(dict(zip(cles,datas)))
            
    return liste

def ecriture(rep, liste, delimiter = ";"):
    
    with open (rep, "w") as csvfile:
        ligneDesc = ";".join(liste[0].keys()) + "\n"
        csvfile.write (ligneDesc)
        
        for cle in range(len(liste)):
            ligne = ";".join(liste[cle].values()) + "\n"
            csvfile.write (ligne)