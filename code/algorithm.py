from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
import pandas as pd
import numpy as np
import random
import re

df = pd.read_csv('D:\Coding\IT_ticket_automation\data\\no_name_distance_matrix.csv',index_col=0)
names = pd.read_csv('D:\Coding\IT_ticket_automation\data\\distance_matrix.csv',index_col=0)
time_info = pd.read_csv('D:\Coding\IT_ticket_automation\data\\finished_data.csv',index_col=0)
# print(time_info)
df_names = pd.DataFrame({
    'Name': time_info.index,
    'Number': df.index,
    'Time': time_info.class_open
})
df_names.reset_index()
print(df_names)
num_rooms = int(input('How many rooms are you going to: '))
time = float(input('what time are you leaving at: '))
time = time * 4
time = int(time)
names_list = ['UO130']

# for i in range(num_rooms-1):
#     val = input(f'Please Type the name of room {i+1} of {num_rooms}: ')
#     names_list.append(val)

no_uo = list(names.columns)
no_uo.remove('UO130')
names_list.extend(random.choices(no_uo, k=num_rooms))


location_list = []
for i in names_list:
    location = names.index.get_loc(i).item()
    location_list.append(str(location))

df_mat_dist = df[location_list]
int_location_list = [int(x) for x in location_list]
df_mat_dist = df_mat_dist.loc[int_location_list]


closest_idx = list(names.columns).index('UO130')
closest_idx = int(closest_idx)

npoints = len(df_mat_dist)
path_points = [closest_idx]
path_length = 0


n = 0
location = time
for _ in range(npoints-1):
    room_info=df_names.loc[df_names['Number'] == closest_idx, 'Time'].item()
    room_info = re.sub(r"[\([{})\]]", "", room_info)
    room_info = [int(item) for item in room_info.split(',')]
    other_rooms = df_names.loc[(df_names['Number'] != closest_idx)&(df_names['Number'].isin(int_location_list))]


    num = 0
    other_room_time = []
    other_room_names = []
    for i in range(len(other_rooms)):
        name = other_rooms.iloc[i]
        room_info = other_rooms.iloc[i]['Time']
        room_info = re.sub(r"[\([{})\]]", "", room_info)
        room_info = [int(item) for item in room_info.split(',')]
        other_room_time.append(room_info)
        other_room_names.append(name[0])

    weight = 1
    for room in range(len(other_room_time)):
        isopen = other_room_time[room][location+num]
        while isopen == 0:
            num = num + 1
            isopen = other_room_time[room][location+num]
            weight = weight + 10
        num = num + 1
    


    closest_dist = df_mat_dist.loc[closest_idx, ~df_mat_dist.index.isin(other_room_names)]
    closest_idx = df_mat_dist.loc[closest_idx, ~df_mat_dist.index.isin(path_points)].idx()
    print('closest dist')
    print(closest_dist)
    print(closest_idx)
        
    
    closest_dist = df_mat_dist.loc[closest_idx, ~df_mat_dist.index.isin(path_points)].min()
    
    closest_idx = df_mat_dist.loc[closest_idx, ~df_mat_dist.index.isin(path_points)].idxmin()
    closest_idx = int(closest_idx)
    
    path_points.append(closest_idx)
    path_length += closest_dist
    if closest_idx != 255:
        location = location +1
    print(location/4)
true_path = []
for i in path_points:
    item=df_names.loc[df_names['Number'] == i, 'Name'].item()
    true_path.append(item)

# print(path_points, path_length)
print('The best order to go to these rooms is:')
print(true_path)


