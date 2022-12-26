from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


#initialize global variables
PATH = '~/.local/bin/chromedriver'
OPTIONS = Options()
#open in debugger mode
OPTIONS.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
DRIVER = webdriver.Chrome(PATH, options=OPTIONS)


def launch_browser():
    '''Run debugger-mode, sign into Tinder, accept default cookie settings, follow pre_requisite.md then begin auto-swiping in Tinder.'''
    DRIVER.get('https://tinder.com/app/recs')
 
    sleep(5)
    heart_button = DRIVER.find_element(By.XPATH, '//*[@id="s-1602360476"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
    for n in range(80):
        sleep(3)
        try:
            heart_button.click()
        except ElementClickInterceptedException:
            try:
                sleep(5)
                match_popup = DRIVER.find_element(By.XPATH, '//*[@id="s-1271989275"]/main/div/div[1]/div/div[4]/button')
                match_popup.click()
            except NoSuchElementException:
                sleep(2)


#initialize selenium browser
try:
    launch_browser()

except KeyboardInterrupt:
    print('See you later.')