import pandas as pd
import os
import logging
import re
from time import sleep
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constantes import CURRENT_DATE, ceps
from utils.chrome import start_driver

def get_print(driver, cod, estado, folder_prints="prints"):
    sleep(2)
    dir_caminho = os.path.abspath(
        folder_prints) + f'\\{cod}_{estado}_{CURRENT_DATE}.png'
    driver.save_screenshot(dir_caminho)

def get_price(driver, price_element):
    sleep(0.5)
    price_ = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, price_element))).text
    regex = re.findall(r'\d+\.\d+', price_.replace(",", "."))[0]
    return regex

def close_popup(driver):
    try:
        # botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-close")))
        # botao.click()

        aceitar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "close-icon")))
        aceitar.click()
    except:
        pass

def add_cep(driver, encomenda, i):
    sleep(4)
    uf = encomenda['ESTADO'][i]
    cep = ceps[uf]
    input_cep = driver.find_element(By.CSS_SELECTOR, ".relative.w-full.flex.base-input.transition.duration-300.ease.pl-1.bg-transparent input")
    input_cep.send_keys(cep)
    input_cep.submit()


def change_location(driver, encomenda, i):
    sleep(1)
    uf = encomenda['ESTADO'][i]
    cep = ceps[uf]
    #close_popup(driver)
    
    try:
        # button_change = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#HEADER_geolocation")))
        # button_change.click()

        box_element = driver.find_elements(By.CSS_SELECTOR, ".form-group.div-input-with-label-floating")

        for item in box_element:
            input_cep = item.find_element(By.CSS_SELECTOR, "#location-search")
            input_cep.send_keys(cep)
            sleep(1)
            
            confirmar = driver.find_element(By.CSS_SELECTOR, "#btnSubmitCep")
            confirmar.click()
            sleep(1)
    except:
        print(f"Sem região para o cep: {uf}->{cep}")

def SCRAPER(encomenda, price_element):
    #creating list
    prices = []
    #starting chrome
    driver = start_driver()
    for i in tqdm(encomenda.index):
        
        #opning url
        driver.get(encomenda['URL DO INSUMO'][i])
        #change_location(driver, encomenda, i)
        #close_popup(driver)
        try:
            #close_popup()
            price = get_price(driver, price_element)
        except:
            price = None
        
        prices.append(price)
        sleep(0.5)
        get_print(driver, encomenda['CD_INSUMO'][i], encomenda['ESTADO'][i])
    
    encomenda['preco_coleta'] = prices
