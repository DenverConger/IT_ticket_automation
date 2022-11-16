from selenium import webdriver
import datetime
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re
import numpy as np
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

val = "http://scheduling.byui.edu/BrowseForSpace.aspx"

browser.get(val)
input("Press enter when ready")
browser.switch_to.window(browser.window_handles[1])
info_dict = {}
room_info = []

# building = browser.find_elements(By.XPATH,"//div[contains(@class,'.building-column')]")
room_column = browser.find_elements(By.CLASS_NAME,"room-column")
    # Get all the elements available with tag name 'p'
# elements = element.find_elements(By.TAG_NAME, 'p')
# building = column.find_elements(By.CLASS_NAME, "building-column")
# text = building.find_elements(By.CLASS_NAME, "column-text")
# elements = browser.find_elements("xpath","//div[@class='.building-column']")
# print(elements)
data = []
for i in room_column:
    building_id = i.get_attribute('data-building-id')
    room_name_id = i.get_attribute('data-room-id')
    title = i.get_attribute('title')
    data.append([building_id,room_name_id,title])
    print(building_id,"   ",room_name_id,"   ",title)
df = pd.DataFrame(data, columns =['building_id', 'room_id','room_name'])
# for tex in text:
#     title = tex.get_attribute('title')
#     print(title)
# room_name_to_id = browser.find_elements(By.CSS_SELECTOR, ".room-column")
room_info = []
events = browser.find_elements(By.CSS_SELECTOR, ".event-container")
for event in events:
    room_id = event.get_attribute('data-room-id')
    location = event.get_attribute('style')
    location = re.findall(r"(\d+)p", location)
    location = int(location[0])
    # location = datetime.timedelta(minutes=location)
    element_attribute_value = event.get_attribute('innerHTML')
    distance = re.findall(r"(\d+)p", element_attribute_value)
    distance = int(distance[0])
    room_info.append([room_id,location,distance])
    print("id of room", room_id)
    print("location from start",location)
    print("length of class in min",distance)
df2 = pd.DataFrame(room_info, columns =['room_id', 'Hour','Length of Class'])
df3 = pd.merge(df, df2, on="room_id")
df3.to_csv('output.csv', index=False)
print(df3.head)
# room_info = np.asarray(room_info)
# np.save("room_time_webscrape.npy",room_info)