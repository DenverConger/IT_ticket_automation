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

from webdriver_manager.chrome import ChromeDriverManager

browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

val = "http://scheduling.byui.edu/BrowseForSpace.aspx"

browser.get(val)
time.sleep(7)
info_dict = {}
room_info = []
events = browser.find_elements(By.CSS_SELECTOR, ".event-container")
for event in events:
    room_id = event.get_attribute('data-room-id')
    location = event.get_attribute('style')
    location = re.findall(r"(\d+)p", location)
    location = int(location[0])
    location = datetime.timedelta(minutes=location)
    element_attribute_value = event.get_attribute('innerHTML')
    distance = re.findall(r"(\d+)p", element_attribute_value)
    distance = int(distance[0])
    room_info.append(room_id,location,distance)
    print("id of room", room_id)
    print("location from start",location)
    print("length of class in min",distance)
