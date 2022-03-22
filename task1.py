import numpy as np
import pandas as pd
import os
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
list_dir('/var/Data_HUT1/2019',list_csv)
frames = []
for i in list_csv:
    try:
        print(i)
        frames.append(pd.read_csv(i))
        print('done')
    except:
        continue
# 
result = pd.concat(frames)
result.reset_index(inplace=True)
print(result.info())
result.columns=['0','1','2','3','4','5','6','7','8','9']
result['liste_de_tags']=np.nan
#result=result[['timestamp','camera_id','individual_id','liste_de_tags']]
result=result[['1','0','3','liste_de_tags']]
js = result.to_json(orient ='columns')
js
def writejsonfile(file):
  with open (str(file)+'.json','w') as f:
    f.write(js)
writejsonfile(MovTrack)
