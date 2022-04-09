import numpy as np
import pandas as pd
import json
import os
import re

# 遍历当前所有文件夹
list_csv=[]
def list_dir(file_dir,list_csv):
    dir_list = os.listdir(file_dir)
    for cur_file in dir_list:
        path = os.path.join(file_dir,cur_file)
        #判断是文件夹还是文件
        if os.path.isfile(path):
            # print("{0} : is file!".format(cur_file))
            dir_files = os.path.join(file_dir, cur_file)
        #判断是否存在.csv文件，如果存在则获取路径信息写入到list_csv列表中
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
list_csv=list_dir('./',list_csv)
#######################################################################################
result=pd.DataFrame()

frames = []
for i in list_csv:
    csv_named=pd.read_csv(i,header=None)
    a=re.match(r"./data_(.*?)_(.*?)_(.*?)_clean.csv", i)
    i='./LMS'+a.group(2)+'LMS/'+a.group(1)+a.group(2)+'_'
    csv_named.insert(0,'name',i)
    frames.append(csv_named)
# 
result = pd.concat(frames)
result=pd.DataFrame(result)


result=result.reset_index(inplace=False)
#result.columns=['0','1','2','3','4','5','6','7','8','9']

result['liste_de_tags']=np.nan

result=result[[1,0,'name',3,'liste_de_tags']]
result=result.rename(columns={1:'debut/fin'})
result=result.rename(columns={0:'identifiant_capteur'})
result=result.rename(columns={3:'identifiant_individu'})
result=result.rename(columns={'name':'LSM_csv_filename'})

LS=[]
ID=0
df_time_strat=''
df_time=df_time_strat
df_time_end=df_time_strat
df_identifiant_individu=''
df_identifiant_capteur=''
df_LSM_csv_filename=''
for index,row in result.iterrows():
    df_time_strat=row['debut/fin']
    df_identifiant_individu=row['identifiant_individu']
    df_identifiant_capteur=row['identifiant_capteur']
    df_LSM_csv_filename=row['LSM_csv_filename']
    break
for index,row in result.iterrows():
    if row['identifiant_individu'] != df_identifiant_individu:
        df_time_end=df_time
        a=re.match(r"(.*?)-(.*?)-(.*?) (.*?):(.*?):(.*?).(.*?)", df_time_strat)
        df_LSM_csv_filename=df_LSM_csv_filename+a.group(4)+'h'+a.group(5)+'_'+str(df_identifiant_individu)
        LS.append([ID,df_identifiant_individu,df_time_strat,df_time_end,df_identifiant_capteur,df_LSM_csv_filename])
        df_identifiant_individu=row['identifiant_individu']
        df_time_strat=row['debut/fin']
        ID+=1
    df_time = row['debut/fin']
    df_identifiant_capteur=row['identifiant_capteur']
    df_LSM_csv_filename=row['LSM_csv_filename']
lsToCsv=pd.DataFrame(LS,columns=['ID','identifiant_individu','time_strat','time_end','identifiant_capteur','LSM_csv_filename'])
lsToCsv.to_csv('demo.csv')




