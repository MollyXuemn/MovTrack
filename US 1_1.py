# -*- coding: utf-8 -*-


"""
creer par jérémy 
"""

"""
Spyder Editor

This is a temporary script file.
"""
"""
"premiere étape chargée les données" 

premirere variable, le nom du dossier
bloucle while, tant que fichier pas traiter
    regarde donnée dedans
    
while fichier existe, 
regarder les données dedans
//

deuxieme étape créer le tableau, dans un deuxieme fichier
if not exist
create table, with column....

troisieme étape, trier les données
donnée précédentes, on enleve les données ou il y a rien


quatrieme étape les mettres dans le bon ordre , avec la bonne forme
donnée précédentes, on prends que quelques colonnes, on en supprime autres...

cinquieme étape, les insérer dans le tableau 
while reste fichier
add donnée précédente dans tableau"
"""
nomfichier="test.txt" 
last_line=""
"""
charge le fichier en question, ecrit en derniere ligne une étoile si dejàn chargé
"""
def chargement(nomfichier):
    with open('nomfichier', 'w') as f:
        last_line = f.readlines()[-1]
        if last_line=="*":
            nomfichier.close
            pass
        else:
            nomfichier.writelines("*")[-1]
            nomfichier.close
            pass
pass
"""
charge le dossier en question
"""
def chargerdossier(nomdossier):
    import os
    absolutepath=""
    path = 'absolute path'
    dir_list = os.listdir(path)
    for i in range(len.dir_list):
        chargement(dir_list[i])
        pass     
pass
"""

"""