import os
import sys

def verifier_fichier(dossier, fichier):
    
    chemin_fichier = os.path.join(dossier, fichier)
    
    confirmation = input ('Appuies sur ENTREE quand c\'est fait !')

    if os.path.isfile(chemin_fichier) == False:
        return False
    else:
        return True

def supprimer_fichier(chemin_fichier):
    try:
        os.remove(chemin_fichier)
    except FileNotFoundError:
        print(f'Le fichier "{chemin_fichier}" n\'existe pas.')
    except Exception as e:
        print(f'Une erreur s\'est produite lors de la suppression du fichier "{chemin_fichier}": {e}')

def fonction_super_mega_speciale_4001():
    
    print ('\nBienvenue dans la fonction spéciale...')
    print ('Je suis désolé mais elle est si importante que je ne peux pas te laisser y accéder...')
    print ('Sauf si... réussis tous ces tests et tu pourras la tester !')
    
    choice1 = input ('\nPresse ESPACE pour commencer !')
    
    if choice1 == '':
        
        print ('\nBien, je vois que tu sais utiliser un clavier, je suis fier de toi !')
        print ('Maintenant, écris : "La caractérisation des personnages dans "Les Caractères" de La Bruyère est profonde et subtile, déployant une observation aiguë de la nature humaine à travers une série de portraits satiriques. La plume incisive de l\'auteur dépeint divers archétypes sociaux du 17ᵉ siècle, offrant une critique mordante des comportements, des vices et des vertus. Les Caractères révèlent une finesse psychologique exceptionnelle, chaque caractère étant une étude minutieuse des travers humains, combinant perspicacité intellectuelle et perspicacité sociale. La Bruyère transcende les particularités temporelles pour créer une œuvre intemporelle qui continue d\'interroger et de refléter la nature humaine à travers ses personnages richement nuancés.')
        
        choice2 = input ('\n Ecris-le là : ')
        
        if choice2 == 'La caractérisation des personnages dans "Les Caractères" de La Bruyère est profonde et subtile, déployant une observation aiguë de la nature humaine à travers une série de portraits satiriques. La plume incisive de l\'auteur dépeint divers archétypes sociaux du 17ᵉ siècle, offrant une critique mordante des comportements, des vices et des vertus. Les Caractères révèlent une finesse psychologique exceptionnelle, chaque caractère étant une étude minutieuse des travers humains, combinant perspicacité intellectuelle et perspicacité sociale. La Bruyère transcende les particularités temporelles pour créer une œuvre intemporelle qui continue d\'interroger et de refléter la nature humaine à travers ses personnages richement nuancés.':
                
            print ('\nBien joué, tu sais copier-coller du texte (j\'espère que tu l\'as fais...)')
            print ('A présent, testons autre chose...')
            print ('Tu vas jouer à un pendu, tu vas devoir trouver le prénom d\'un de tes contacts !')
            
            from c_options.fs.pendu_special import pendu_special
            
            if pendu_special() == True:
                
                print ('\nFélicitations !')
                print ('Allez, encore quelques tests et tu pourras accéder à cette fonction')
                print ('Bon, j\'ai besoin de ton aide, un fichier manque à ce programme... sans lui, on ne peut pas continuer...')
                print ('Diriges toi dans le dossier contenant le repertoire, trouves le fichier "olala_je_suis_utile.txt" et déplaces le dans le dossier fs')
                
                if verifier_fichier('E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\c_options\fs', 'olala_je_suis_utile.txt') == True:
                    
                    print ('\nSuper, on atteint le but !')
                    print ('Une dernière chose...')
                    print ('J\'aimerais que tu effaces une fonction...')
                    print ('La fonction "supprimer()" me dérange, je n\'accepte pas que l\'on puisse supprimer son travail..')
                    
                    if verifier_fichier('E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\c_options', 'supprimer_c.py') == False:
                        
                        print ('\nBien, tu as réussi !')
                        print ('A présent, tu mérites d\'accéder à la fonction spéciale...')
                        
                        print ('\nCe programme à été crée par MESNAGE Dylan et GORLAS Maxime,')
                        print ('avec l\'aide de LEMERCIER Guenaël, ils ont permit que ce projet soit possible,')
                        print ('la toute première version contenée aussi une fonction spéciale, celle-ci mettait fin au repertoire en le réinitialisant...')
                        
                        print ('\nMais cette version fait bien pire !')
                        
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\choix.py")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\depart.py")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\main.py")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\PDN.py")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\a_contacts")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\b_favoris")
                        supprimer_fichier("E:\Lycée (1e)\NSI\0_PROJETS\0_REPERTOIRE\V4\V4.00\0_repertoire\c_options")
                        
                        sys.exit('Fin du programme.')
                    
                
                else:
                    sys.exit('Arrêt du programme (fonction spéciale non accomplie)')
            else:
                sys.exit('Arrêt du programme (fonction spéciale non accomplie)')
        else:
            sys.exit('Arrêt du programme (fonction spéciale non accomplie)')
    else:
       sys.exit('Arrêt du programme (fonction spéciale non accomplie)')
    








choice4 = 'NONE'
choice5 = 'NONE'
choice6 = 'NONE'
choice7 = 'NONE'
choice8 = 'NONE'
choice9 = 'NONE'
choice10 = 'NONE'

fonction_super_mega_speciale_4001()