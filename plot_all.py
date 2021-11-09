import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

labels_path = r'C:\Users\buchh\Desktop\New folder (2)'
files = os.listdir(labels_path)

column_name = 'l'

tracker_id = 6

all_dataframes = []
count = 0
for file in files:
    file_path = os.path.join(labels_path, file)
    data = pd.read_csv(file_path, sep=" ", header=None)
    data.columns = ['label_name','id','h','w','l','y','z','x','orientation','confidence', 'roll', 'pitch', 'yaw'] # change here if columns changes
    frame_number_column = [count] * len(list(data['label_name']))
    data.insert(0, 'Frame_number', value = frame_number_column)
    count = count + 1
    all_dataframes.append(data)

merged_Data = pd.concat(all_dataframes)
merged_Data.to_csv('final_data.csv')
'''
#print(merged_Data)
merged_Data_filtered_tracker_id = merged_Data[merged_Data['id'] == int(tracker_id)]
#print(merged_Data_filtered_tracker_id)
column_data =list(merged_Data_filtered_tracker_id[column_name])
#print(column_data)

plt.plot(column_data)
plt.title(tracker_id)
plt.show()
'''