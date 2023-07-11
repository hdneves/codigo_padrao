from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)

def start_driver():
    
    '''Function to start the driver with personal settings'''

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--able-popup-blocking') 
    options.add_argument('window-size=2560x1440')
    #options.add_argument('window-size=1920x1080')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), chrome_options=options)
    return driver