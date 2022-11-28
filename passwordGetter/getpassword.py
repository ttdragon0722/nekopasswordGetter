#import and general setting
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get():
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # #取得假姓名、電話
    # chrome.get("https://lab.sp88.com.tw/genall/")
    # time.sleep(1)
    # chrome.execute_script("window.scrollTo(0, 1000)")
    # chrome.find_element(By.XPATH,'//*[@id="nm-styler"]').click()
    # chrome.find_element(By.XPATH,'//*[@id="nm-styler"]/div[2]/ul/li[1]').click()
    # time.sleep(1)
    # chrome.find_element(By.XPATH,'//*[@id="btn_submit"]').click()
    # time.sleep(3)
    # name_phone = chrome.find_element(By.XPATH,'//*[@id="result"]').text
    # name_phone = name_phone.split(",")
    name = "雷克斯"
    phone = "0909956502"
    chrome.get("https://docs.google.com/forms/d/e/1FAIpQLSdVPQcXsGtyGne2Inus6AsjD99Y8KSXXMFcP4AIoUhKWCsCFw/viewform")
    # time.sleep(1)

    element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span'))
    )
    
    #info
    chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(name)
    chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phone)
    chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    element = WebDriverWait(chrome, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[3]'))
    )
    # time.sleep(3)
    return chrome.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[3]').text[-5:-1]