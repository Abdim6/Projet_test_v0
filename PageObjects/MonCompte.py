"""
Objectif : Instentier les actions liées à la page mon compte  
Date de la dernière grosse maj : 23/03/2022
Owner : Abdi
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PageObjects.Locator import Locators
from TestCases.conftest2 import action_OnElem

class MonCompte:
    def __init__(self, driver):
        # self.driver = driver
        self.obj = action_OnElem(driver)
    
    def clickgenerInfo(self):
        # self.driver.find_element(Locators.btn_gererInfos_CSS).click()
        self.obj.click(Locators.btn_gererInfos_CSS)

    def clickModifier(self):
        # self.driver.find_element(Locators.btn_modifier_CSS).click()
        self.obj.click(Locators.btn_modifier_CSS)

    def setPrenom(self, prenom):
        # self.driver.find_element(Locators.textbox_firstname_id).clear()
        # time.sleep(1)
        # self.driver.find_element(Locators.textbox_firstname_id).send_keys(prenom)
        self.obj.enter_text(Locators.textbox_firstname_id,prenom)

    def setNom(self, nom):
        # self.driver.find_element(Locators.textbox_lastname_id).clear()
        # self.driver.find_element().send_keys(nom)
        self.obj.enter_text(Locators.textbox_lastname_id,nom)

    def clickValider(self):
        # self.driver.find_element(Locators.btn_valider_CSS).click()
        self.obj.click(Locators.btn_valider_CSS)
  