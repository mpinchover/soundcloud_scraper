"""
# activate env 
source soundcloud_scraper/bin/activate

# install reqs
pip install -r requirements.txt
"""
import requests
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from chromedriver_py import binary_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


def play_soundcloud_track(driver):
    print("Loading soundcloud page")
    driver.get("https://soundcloud.com/pinch-12/track-20")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "title")))
    soup = BeautifulSoup(driver.page_source, "html.parser")

    try:
        print("Attempting to play song now")
        play_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "sc-button-play"))
        )
        play_button.click()
        print("Playing song now")
    except Exception as e:
        print(f"An error occurred: {e}")


def run_scraper():
    print("Loading driver")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    svc = ChromeService(ChromeDriverManager().install())

    # svc = webdriver.ChromeService(executable_path=binary_path, options=options)
    driver = webdriver.Chrome(service=svc, options=options)
    play_soundcloud_track(driver)
    time.sleep(300)

    driver.quit()

if __name__ == "__main__":
    run_scraper()