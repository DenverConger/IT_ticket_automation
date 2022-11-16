import numpy as np
import pandas as pd
import re
building_dict = {
    1: "Agriculture Engineering Building",
    2: "Austin",
    3: "Benson",
    4: "Clarke",
    5: "Hart",
    6: "Hinckley",
    8: "Kimball",
    12: "Manwaring Center",
    13: "McKay Library",
    14: "Ricks",
    15: "Rigby",
    16: "Romney",
    17: "Smith",
    18: "Snow",
    19: "Spori",
    20: "Stadium",
    22: "Taylor",
    24: "Fields",
    29: "Thomas E Ricks Gardens",
    35: "Engineering Technology Center",
    45: "BYU-Idaho Center",
    47: "Biddulph Hall",
    88: "Amphitheatre & Plaza Quads",
    217: "Sky Mountain Ranch",
    239: "Science and Technology Center"
}

abbr_building_dict = {
    1: "AGM",
    2: "AUS",
    3: "BEN",
    4: "CLK",
    5: "HRT",
    6: "HIN",
    8: "KIM",
    12: "MAN",
    13: "MCK",
    14: "RKS",
    15: "RIG",
    16: "ROM",
    17: "SMI",
    18: "SNO",
    19: "SPO",
    20: "",
    22: "TAY",
    24: "",
    29: "",
    35: "ETC",
    45: "",
    47: "",
    88: "",
    217: "",
    239: "STC"
}
print(building_dict.get(88))
df = pd.read_csv("D:\Coding\IT_ticket_automation\output.csv", index_col=False)

print(df.head(50))
df['building_name'] = df['building_id']
df['building_name'].replace(building_dict, inplace=True)
df['abbr_building_name'] = df['building_id']
df['abbr_building_name'].replace(abbr_building_dict, inplace=True)

def split_it(year):
    return re.findall('^([-\S]+)', year)[0]

df['class_number'] = df['room_name'].apply(lambda x: split_it(x))
df["Full Name of Space"] = df["abbr_building_name"] + df["class_number"]

# df = df[["Full Name of Space","Hour", "Length of Class", "room_id"]]
df2 = pd.read_csv("D:\Coding\IT_ticket_automation\mastaroomlistexcel.csv", index_col=False)
df3 = pd.merge(df2, df, on="Full Name of Space")

print(df.head(50))
df.to_csv('cleaned_output.csv', index=False)
df3.to_csv('merged_data.csv', index=False)
