import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class DownloadMusic(object):
    """
    Class that handles the finding and downloading of a youtube usic video
    """

    SongURL = ''
    
    def __init__(self,SongName):
        self.SongName = SongName
        self.SongURL = ''

    def FindYoutubeVideo(self):
        driver.get("https://www.youtube.com/")
        driver.find_element_by_name("search_query").send_keys(self.SongName+Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_id("video-title").click()
        self.SongURL=driver.current_url

    def DownloadSong(self):
        if(self.SongURL != ''):
            
            driver.get("https://x2convert.com/download-youtube-to-mp3-music")
            driver.find_element_by_id("txtLink").send_keys(self.SongURL+Keys.RETURN)
            time.sleep(10)
            driver.find_element_by_id("btnDown").click()

        else:
            print("An error occured while getiing the url!!")



    
    pass


if __name__ == "__main__":
    
    val = input("Song Name: ")  
    PATH=".\chromedriver.exe"
    driver=webdriver.Chrome(PATH)
    YT = DownloadMusic(val)
    YT.FindYoutubeVideo()
    YT.DownloadSong()

    pass

