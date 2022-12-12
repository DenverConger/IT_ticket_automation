import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist
from scipy.spatial import distance
df = pd.read_csv('D:\Coding\IT_ticket_automation\data\\fully_wrangled_data.csv')
print(df)
df['hours_open'] =df["hours_open"].str.split("-").apply(lambda x: [int(i) for i in x])

# df.hours_open = df.hours_open.to_numpy(dtype='int32')
df['length_per_class'] = df["length_per_class"].str.split("-").apply(lambda x: [int(i) for i in x])
df["class_open"] = np.array

generic_class_open = []


for i in range(len(df)):
    class_open = []
    for j in range(0,1440,15):
        # if the 15 min icrement is in the hours open
        if (j > 0) and (len(class_open)*15 > j):
            x = 1
        elif j not in df['hours_open'][i]:
            class_open.append(1)
            
        elif j in df['hours_open'][i]:
            #index location of the hours open in list
            location = df['hours_open'][i].index(j)
            #legth of class in min
            length_class = df['length_per_class'][i][int(location)]
            inc_15 = j // 15
            # print(inc_15)
            per_15 = length_class // 15
            # print(per_15)
            # print('Classtime',inc_15)
            # print('Classtime plus class',inc_15+per_15)
            # print((inc_15+per_15)-inc_15)
            for k in range(inc_15,inc_15+per_15):
                class_open.append(0)
    df.at[i, 'class_open'] = class_open
indeer = 1
print(df)
print(df.hours_open[indeer])
print(df.length_per_class[indeer])
print(df.class_open[indeer])
print(df['Full Name of Space'][indeer])
locat = [i for i, x in enumerate(df.class_open[indeer]) if x]
print(locat)
for i in locat:
    value = i / 4
    print(i,value)

df = df.drop('hours_open', axis=1)
df = df.drop('length_per_class', axis=1)


name_of_space = "UO130"
building = 0
room = 0 
X1 = -111.78555115417132
Y1 = 43.81621251885974
listinfo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# print(df)
df2 = df.append(pd.DataFrame([[name_of_space,X1,Y1,building,room,listinfo]], columns=df.columns))
df2.to_csv('D:\Coding\IT_ticket_automation\data\\finished_data.csv', index=False)
df_array = df2[["Y", "X"]].to_numpy()
dist_mat = cdist(df_array, df_array,'euclidean')


# 
# dist_mat = pd.DataFrame(dist_mat)
# aus1 = dist_mat.loc[dist_mat["AUS009"]]

# print(distance.cdist(dist_mat,s2).min(axis=1))
df3 = pd.DataFrame(dist_mat, columns = df2["Full Name of Space"], index = df2["Full Name of Space"])
df4 = pd.DataFrame(dist_mat)
names_to_explore = ['AUS009','CLK143','TAY249']
total_dist = 0
for j in range(len(names_to_explore)):
    locations = df3.loc[names_to_explore[j] , [x for i,x in enumerate(names_to_explore) if i!=j]]
    print(locations)
    total_dist = total_dist + locations

print(total_dist)
df3.to_csv('D:\Coding\IT_ticket_automation\data\distance_matrix.csv', index=True)
df4.to_csv('D:\Coding\IT_ticket_automation\data\\no_name_distance_matrix.csv', index=True)
