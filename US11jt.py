# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:05:28 2022

@author: jeremy
"""
def US11():

    # i=0
    # d=0
    # listdist=[]
    # for i in coordSpineMid:
    #     d=math.sqrt(((coordSpineMid[2+i]-coordSpineMid[i])**2)+((coordSpineMid[3+i]-coordSpineMid[1+i])**2))
    #     d.extend(listdist)

    # print(listdist)
    import re
    import math
    import numpy as np
    import pandas as pd
    import os
    # 遍历当前所有文件夹
    #boucle dans tous les dossiers actuels
    list_csv=[]
    def list_dir(file_dir,list_csv):
        dir_list = os.listdir(file_dir)
        for cur_file in dir_list:
            path = os.path.join(file_dir,cur_file)
            #判断是文件夹还是文件
            # Déterminez s'il s'agit d'un dossier ou d'un fichier
            if os.path.isfile(path):
                # print("{0} : is file!".format(cur_file))
                dir_files = os.path.join(file_dir, cur_file)
            #判断是否存在.csv文件，如果存在则获取路径信息写入到list_csv列表中
            #Déterminez s'il existe un fichier .csv, si c'est le cas, obtenez les informations de chemin et écrivez-les dans la liste list_csv
            if os.path.splitext(path)[-1] == '.csv':
                csv_file = os.path.join(file_dir, cur_file)
                # print(os.path.join(file_dir, cur_file))
                # print(csv_file)
                list_csv.append(csv_file)
            if os.path.isdir(path):
                # print("{0} : is dir".format(cur_file))
                # print(os.path.join(file_dir, cur_file))
                list_dir(path,list_csv)
                
        return list_csv

    list_dir('/var/Data_HUT1/2019',list_csv)
    frames = []
    for i in list_csv:
        try:
            print(i)
            frames.append(pd.read_csv(i))
            print('done')
        except:
            continue
     
    #traitement des données, afin éviter les doublons
    with list_dir as f:
        line = f.readline().rstrip()
        #regarde la ligne l
        line1= f.readline().rstrip()[1]
        #regarde la ligne l+1
        vraiecoordonnée=[]
        
        while line:
            elmtligne=re.split(",", line)
            elmtligne1=re.split(",", line1)
            #coordonnées ligne 1 et0
            vraiecoordonnée=[line]
            
            if getDifference(elmtligne[1],elmtligne1[1])[4]>1:
                #si la durée entre deux mesure est supérieure à 1 minute
                vraiecoordonnée.extend(line1)
            if elmtligne[0] !=elmtligne1[0]:
                #si on change utilisateur
                vraiecoordonnée.extend(line1)           
        line = f.readline().rstrip()
    f.close()
    
    for i in vraiecoordonnée:
        try:
            print(i)
            frames.append(pd.read_csv(i))
            print('done')
        except:
            continue
     
    #injections dans la base de données
    result = pd.concat(frames)
    result.reset_index(inplace=True)
    print(result.info())
    result.columns=['0','1','2','3','4','5','6','7','8','9']
    result['liste_de_tags']=np.nan
    result['skeleton.csv']='LMS'+'1'+'liste_de_tags'
    #result=result[['timestamp','camera_id','individual_id','liste_de_tags']]
    result=result[['1','3','0','liste_de_tags','skeleton.csv']]
    js = result.to_json(orient ='columns')
    js
    def writejsonfile(file):
      with open (str(file)+'.json','w') as f:
        f.write(js)
    writejsonfile(MovTrack)

from datetime import datetime

def getDifference(then, now = datetime.now(), interval = "secs"):

    duration = now - then
    duration_in_s = duration.total_seconds() 
    
    #Date and Time constants
    yr_ct = 365 * 24 * 60 * 60 #31536000
    day_ct = 24 * 60 * 60 			#86400
    hour_ct = 60 * 60 					#3600
    minute_ct = 60 
    
    def yrs():
      return divmod(duration_in_s, yr_ct)[0]

    def days():
      return divmod(duration_in_s, day_ct)[0]

    def hrs():
      return divmod(duration_in_s, hour_ct)[0]

    def mins():
      return divmod(duration_in_s, minute_ct)[0]

    def secs(): 
      return duration_in_s

    return {
        'yrs': int(yrs()),
        'days': int(days()),
        'hrs': int(hrs()),
        'mins': int(mins()),
        'secs': int(secs())
    }[interval]
