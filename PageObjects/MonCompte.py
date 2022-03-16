"Ce fichier a pour objectif de localiser les objets de la page OB"
"& une classe qui permetra d'éffectuer la connexion"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators

class MonCompte:
    def __init__(self, driver):
        self.driver = driver
    
    def clickgenerInfo(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.btn_gererInfos_CSS).click()

    def clickModifier(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.btn_modifier_CSS).click()

    def setPrenom(self, prenom):
        self.driver.find_element(By.ID,Locators.textbox_firstname_id).clear()
        time.sleep(1)
        self.driver.find_element(By.ID,Locators.textbox_firstname_id).send_keys(prenom)

    def setNom(self, nom):
        self.driver.find_element(By.ID,Locators.textbox_lastname_id).clear()
        self.driver.find_element(By.ID,Locators.textbox_lastname_id).send_keys(nom)

    def clickValider(self):
        self.driver.find_element(By.CSS_SELECTOR,Locators.btn_valider_CSS).click()

  