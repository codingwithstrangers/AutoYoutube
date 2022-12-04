import json
import time
import os
from select import select
from selenium.webdriver.common.by import By
import get_yt_url
from selenium.webdriver.support.ui import Select
from selenium import webdriver

import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options



#this is how I call the title and desc.(turn to False when testing)
yt_video = get_yt_url.download_youtube_url("https://youtu.be/leLqD96CEQQ", download=True)
print(yt_video.title)
print(yt_video.description)


def get_login(key):
    with open("creds.json") as f:
        json_load = json.load(f)
        return json_load[key]


# print(get_login("username"))
# exit()

#this is how I stop the window from closing while testing
# chromedriver_autoinstaller.install()
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

#run proper script for non test
driver = webdriver.Chrome()
driver.get("https://anchor.fm/login")
# assert "Python" in driver.title

#this is how I enter my username, password and submit
print("User Name and Password Done")
driver.find_element("xpath", '//*[@id="email"]').send_keys(get_login("username"))
time.sleep(1)
driver.find_element("xpath", '//*[@id="password"]').send_keys(get_login("password"))
time.sleep(1)
driver.find_element("xpath", '//*[@id="LoginForm"]/div[3]/button').click()
time.sleep(3)


#this is how I add a new podcast and submit the type
print('Podcast has been dragged and dropped')
driver.find_element("xpath", '//*[@id="app"]/div/nav/div/div/div/div[1]/div[3]/div/div[1]/div/button').click()
time.sleep(1)
driver.find_element("xpath", '//*[@id="app"]/div/nav/div/div/div/div[1]/div[3]/div/div[1]/div/div/div/div/a/div').click()
time.sleep(3)


#this is how I select the podcast from my files
print('m4a should be loading on site')
driver.find_element("xpath", '//*[@id="app-content"]/div/div/div/div/div[2]/div/div/input').send_keys("F:\Coding with Strangers\AutoYoutube\podcast.m4a")
time.sleep(2)


#while loop for checking if Save Button is active
print('Loop for save button works')
save = driver.find_element("xpath", '//*[@id="app-content"]/div/div/div/div/div[2]/button')
while save.get_attribute("disabled"):
    time.sleep(5)
save.click()


#insert ad button 1 (this was a hoe... used JS ato look under hood)and save
print('JS script is running stderr')
time.sleep(5)
stderr = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/div[7]/div/button')
driver.execute_script("arguments[0].click();", stderr)
time.sleep(3)


#this is how you select an insert ad number from dropdown
print('add ad clicking button works')
pick = Select(driver.find_element(By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/select'))
pick.select_by_value("1")
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/button').click()
time.sleep(3)

#alertbox pops up this is the code for it
print('pop up ad button in window')
driver.find_element(By.XPATH, '/html/body/reach-portal[2]/div[2]/div/div/div/div[2]/div/button[2]').click()

#submit ad final step
print('submit ad to youtube final ')
driver.find_element(By.XPATH, '/html/body/reach-portal/div[2]/div/div/div/div[2]/div/div[3]/div[2]/button').click()


#add title and description
print('Submitting YoutTube Video Title and description to Anchor')
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/div[3]/div[2]/input').send_keys(yt_video.title)
driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/div[4]/div[2]/div[2]/div/div/div[2]/div/div[2]/div').send_keys(yt_video.description)

# submit for save later
print('save for later... last part of script')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/form/div[1]/div[2]/button[1]').click()

#delete m4a
print('Machine made me write this because he is sure in 6 months I will forget that this means the file is deleted')
time.sleep(3)
os.remove('F:\Coding with Strangers\AutoYoutube\podcast.m4a')


#Fin
print('thats all folks')


