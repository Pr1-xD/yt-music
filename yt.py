import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

val = input("Song Name: ")  
PATH=".\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys(val+Keys.RETURN)
driver.find_element_by_id("video-title").click()
song=driver.current_url
driver.get("https://x2convert.com/download-youtube-to-mp3-music")
driver.find_element_by_id("txtLink").send_keys(song+Keys.RETURN)
time.sleep(10)
driver.find_element_by_id("btnDown").click()


# driver.find_element_by_name("Search").send_keys("test" + Keys.RETURN)   